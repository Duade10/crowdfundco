from rest_framework.views import APIView
from rest_framework.response import Response
from .models import RealEstateListing
from .serializers import RealEstateListingSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, CreateAPIView


class CreateRealEstateListing(CreateAPIView):
    def post(self, request):
        serializer = RealEstateListingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListRealEstateListingView(ListAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer


class UpdateRealEstateListingView(RetrieveUpdateAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer
