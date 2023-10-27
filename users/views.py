from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.login_method = "email"
            user.is_active = False
            user.verify_email(request)
            serializer = UserRegistrationSerializer(user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.authtoken.models import Token

# class UserRegistrationView(APIView):
#     def post(self, request, format=None):
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             user.is_active = False
#             user.verify_email(request)
#             # Create a token for the user
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
