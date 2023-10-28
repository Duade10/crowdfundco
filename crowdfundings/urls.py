from django.urls import path

from . import views


urlpatterns = [
    path("create-campaign/", views.CampaignCreateView.as_view()),
    path("campaign/<int:pk>/detail/", views.CampaignDetailView.as_view()),
    path("campaign/<int:campaign_id>/progress/", views.CampaignProgressView.as_view(), name="campaign-progress"),
]
