from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RealEstateListing
from .serializers import RealEstateListingSerializer, RealEstateListingCreateSerializer
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework import permissions


class CreateRealEstateListing(CreateAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRealEstateListingListView(ListAPIView):
    serializer_class = RealEstateListingSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = RealEstateListing.objects.filter(real_estate_agent=user)
            return queryset


class ListRealEstateListingView(ListAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer


class RealEstateListingViewRetrieveView(RetrieveAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer


class UpdateRealEstateListingView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingCreateSerializer


class DeleteRealEstateListingView(DestroyAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer
