from rest_framework import serializers
from .models import CrowdfundingCampaign, CampaignUpdate
from realestatelistings.models import RealEstateListing
from realestatelistings.serializers import RealEstateListingSerializer
from users.serializers import UserSerializer


class CrowdfundingCampaignDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrowdfundingCampaign
        fields = [
            "title",
            "description",
            "funding_target",
            "start_date",
            "end_date",
            "organizer",
            "status",
            "realestatelisting",
        ]


class CrowdfundingCampainCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrowdfundingCampaign
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["organizer"] = request.user
        real_estate_listing_id = validated_data.get("realestatelisting")
        real_estate_listing = RealEstateListing.objects.get(id=real_estate_listing_id.id)
        campaign = CrowdfundingCampaign.objects.create(**validated_data)
        campaign.title = f"Campaign for {real_estate_listing.title}"
        campaign.funding_target = real_estate_listing.price
        campaign.save()
        return campaign


class CampaignUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignUpdate
        fields = "__all__"
