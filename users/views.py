from rest_framework.views import APIView, status, Request, Response
from users.serializers import UserSerializer

from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
