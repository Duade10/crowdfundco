from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserUpdateSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.login_method = "email"
            user.is_active = False
            # user.verify_email(request)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get("email")
        username = email.split("@")[0]
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request, format=None):
        request.auth.delete()
        return Response({"message": "User logged out"}, status=status.HTTP_200_OK)


class UserUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):
        user = request.user
        user.delete()
        return Response({"message": "User account deleted"}, status=status.HTTP_204_NO_CONTENT)
