from django.urls import path

from petstagram.accounts.views import login_user, logout_user,RegisterView, ProfileDetailsView

urlpatterns = (
    path('login/', login_user, name='log in'),
    path('logout/', logout_user, name='log out'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
)