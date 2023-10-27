from django.urls import path

from . import views


urlpatterns = [
    path("crowdfunding/", views.CampaignListCreateView.as_view()),
    path("crowdfunding/detail/<int:pk>/", views.CampaignListCreateView.as_view()),
    path("campaigns/<int:campaign_id>/progress/", views.CampaignProgressView.as_view(), name="campaign-progress"),
]