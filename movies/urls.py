from django.urls import path
from .views import MovieView, MovieDetailedView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailedView.as_view()),
]
