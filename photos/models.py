from django.core.validators import MinLengthValidator
from django.db import models

from photos.validators import FileSizeValidator


# Create your models here.
class Photo(models.Model):
    MAX_FILE_SIZE: int = 5

    photo = models.ImageField(
        upload_to='media',
        validators=[
            FileSizeValidator(MAX_FILE_SIZE)
        ]
    )
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(limit_value=10)
        ],
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=30
    )

    tagged_pets = models.ManyToManyField(
        to='pets.Pet',
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True
    )