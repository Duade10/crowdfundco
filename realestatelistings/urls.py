from django.urls import path

from . import views

urlpatterns = [
    path("create-real-estate-listing/", views.CreateRealEstateListing.as_view(), name="create-real-estate-listing"),
]
