from django.urls import path
from .views import UserView, LoginJWTView, UserDetailedView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", LoginJWTView.as_view()),
    path("users/<int:user_id>/", UserDetailedView.as_view()),
]
