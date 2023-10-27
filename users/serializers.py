from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            facebook_profile=validated_data["facebook_profile"],
            twitter_profile=validated_data["twitter_profile"],
            linkedin_profile=validated_data["linkedin_profile"],
            user_type=validated_data["user_type"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
