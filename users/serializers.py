from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        username = validated_data["email"].split("@")[0]
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=username,
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "login_method",
            "facebook_profile",
            "twitter_profile",
            "linkedin_profile",
            "receive_notifications",
            "user_type",
        )
