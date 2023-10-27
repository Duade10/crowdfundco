from rest_framework import serializers
from .models import CrowdfundingCampaign, CampaignUpdate


class CrowdfundingCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrowdfundingCampaign
        fields = "__all__"


class CampaignUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignUpdate
        fields = "__all__"
