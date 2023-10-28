from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer

from .models import RealEstateListing


class RealEstateListingCreateSerializer(ModelSerializer):
    class Meta:
        model = RealEstateListing
        fields = (
            "title",
            "description",
            "price",
            "location",
            "property_type",
            "features",
            "status",
            "real_estate_agent",
            "slug",
            "latitude",
            "longitude",
            "size",
            "photo",
        )

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["real_estate_agent"] = request.user
        photo = validated_data["photo"]
        if photo:
            validated_data["photo"] = photo
        listing = RealEstateListing.objects.create(**validated_data)
        return listing


class RealEstateListingSerializer(ModelSerializer):
    real_estate_agent = UserSerializer()

    class Meta:
        model = RealEstateListing
        fields = (
            "id",
            "title",
            "description",
            "price",
            "location",
            "property_type",
            "features",
            "status",
            "slug",
            "latitude",
            "longitude",
            "size",
            "photo",
            "real_estate_agent",
        )
