from rest_framework import generics, permissions
from .models import CrowdfundingCampaign, Contribution
from .serializers import CrowdfundingCampaignDetailSerializer, CrowdfundingCampaignCreateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from .paginations import CampaignPagination


class UserCampaignListView(generics.ListAPIView):
    serializer_class = CrowdfundingCampaignDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CampaignPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = CrowdfundingCampaign.objects.filter(organizer=user)
            return queryset


class CampaignListView(generics.ListAPIView):
    queryset = CrowdfundingCampaign.objects.all()
    serializer_class = CrowdfundingCampaignDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CampaignPagination


class CampaignCreateView(generics.CreateAPIView):
    queryset = CrowdfundingCampaign.objects.all()
    serializer_class = CrowdfundingCampaignCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class CampaignDetailView(generics.RetrieveAPIView):
    queryset = CrowdfundingCampaign.objects.all()
    serializer_class = CrowdfundingCampaignDetailSerializer
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

        serializer = CrowdfundingCampaignDetailSerializer(campaign)

        response_data = {
            "campaign_details": serializer.data,
            "progress_percentage": progress_percentage,
            "total_contributions": total_contributions,
        }

        return Response(response_data)
