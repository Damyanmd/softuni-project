from django.contrib.auth import get_user_model
from django.db import models

from cloudinary import models as cloudinary_models

UserModel = get_user_model()

class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'DOG'),
        (TYPE_CHOICE_CAT, 'CAT'),
        (TYPE_CHOICE_PARROT, 'PARROT'),
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=20,
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = cloudinary_models.CloudinaryField(
        resource_type='image',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )