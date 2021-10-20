from django.urls import path

from petstagram.pets.views import list_pets, like_pet, create_pet, edit_pet, delete_pet, \
    PetDetailsView, CommentPetView

urlpatterns = [
    path('', list_pets, name='list pets'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='pet details'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
    path('comment/<int:pk>', CommentPetView.as_view(), name='comment pet'),
]