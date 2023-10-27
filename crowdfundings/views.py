from rest_framework import generics, permissions
from .models import CrowdfundingCampaign, Contribution
from .serializers import CrowdfundingCampaignSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum


class CampaignListCreateView(generics.ListCreateAPIView):
    queryset = CrowdfundingCampaign.objects.all()
    serializer_class = CrowdfundingCampaignSerializer
    permission_classes = [permissions.IsAuthenticated]


class CampaignDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CrowdfundingCampaign.objects.all()
    serializer_class = CrowdfundingCampaignSerializer
    permission_classes = [permissions.IsAuthenticated]


class CampaignProgressView(APIView):
    def get(self, request, campaign_id):
        try:
            campaign = CrowdfundingCampaign.objects.get(pk=campaign_id)
        except CrowdfundingCampaign.DoesNotExist:
            return Response({"message": "Campaign not found"}, status=404)

        total_contributions = (
            Contribution.objects.filter(campaign=campaign).aggregate(total_contributions=Sum("amount"))[
                "total_contributions"
            ]
            or 0
        )
        progress_percentage = (total_contributions / campaign.funding_target) * 100

        serializer = CrowdfundingCampaignSerializer(campaign)

        response_data = {
            "campaign_details": serializer.data,
            "progress_percentage": progress_percentage,
            "total_contributions": total_contributions,
        }

        return Response(response_data)
