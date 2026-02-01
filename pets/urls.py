from django.urls import path, include

urlpatterns = (
    path('add/', ),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', ),
        path('edit/', ),
        path('delete/', )
    ]))
)