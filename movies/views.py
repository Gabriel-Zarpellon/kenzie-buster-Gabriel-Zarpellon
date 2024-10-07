from rest_framework.views import APIView, status, Response, Request
from .serializers import MovieSerializer
from .models import Movie
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsUserAllowed

from kenzie_buster.pagination import CustomPageNumberPagination


class MovieView(APIView, CustomPageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAllowed]

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies, request, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class MovieDetailedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserAllowed]

    def get(self, request: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
