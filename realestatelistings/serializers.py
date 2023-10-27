from rest_framework.serializers import ModelSerializer

from .models import RealEstateListing


class RealEstateListingSerializer(ModelSerializer):
    class Meta:
        model = RealEstateListing
        fields = "__all__"
