from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.serializers import UserSerializer

from .models import RealEstateListing, ExtraDocument, Image, TokenDetail


class TokenDetailSerializer(ModelSerializer):
    class Meta:
        model = TokenDetail
        fields = "__all__"


class ExtraDocumentSerializer(ModelSerializer):
    class Meta:
        model = ExtraDocument
        fields = ["id", "document_type", "description", "listing", "file"]


class ExtraDocumentCreateSerializer(ModelSerializer):
    class Meta:
        model = ExtraDocument
        fields = ["document_type", "description", "listing", "file"]


class RealEstateListingCreateSerializer(ModelSerializer):
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
            "real_estate_agent",
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
    real_estate_agent = UserSerializer(read_only=True)
    extra_documents = SerializerMethodField()

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
            "latitude",
            "longitude",
            "size",
            "photo",
            "real_estate_agent",
            "extra_documents",
        )

    def get_extra_documents(self, obj):
        extra_documents = obj.extra_documents.all()
        serializer = ExtraDocumentSerializer(extra_documents, many=True)
        return serializer.data
