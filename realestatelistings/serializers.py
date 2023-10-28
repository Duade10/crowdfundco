from rest_framework.serializers import ModelSerializer

from .models import RealEstateListing


class RealEstateListingSerializer(ModelSerializer):
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
