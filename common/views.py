from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.forms import CommentForm, SearchForm
from common.models import Like, Comment
from photos.models import Photo


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    form = SearchForm(request.GET or None)
    photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').all()

    if request.GET and form.is_valid():
        searched_name = form.cleaned_data['pet_name']
        photos = photos.filter(tagged_pets__name__icontains=searched_name)

    context = {
        'photos': photos
    }

    return render(request, 'common/home-page.html', context)


def add_comment(request: HttpRequest, photo_pk: int) -> HttpResponse:
    if request.method == "POST":
        photo = Photo.objects.get(pk=photo_pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{photo_pk}')



def like_functionality(request: HttpRequest, photo_pk: int) -> HttpResponse:
    liked = Like.objects.filter(
        to_photo_id=photo_pk
    ).first()

    if liked:
        liked.delete()
    else:
        Like.objects.create(to_photo_id=photo_pk)

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_pk}')


def share_functionality(request: HttpRequest, photo_pk: int) -> HttpResponse:
    copy(request.META.get('HTTP_REFERER')[:-1] + resolve_url('photos:details', photo_pk))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_pk}')