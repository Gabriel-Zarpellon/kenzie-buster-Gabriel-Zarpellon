from rest_framework.views import APIView, status, Response, Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from movies.models import Movie
from .serializers import MovieOrderSerializer


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, movie_id: int):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie, user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
