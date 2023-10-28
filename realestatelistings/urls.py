from django.urls import path

from . import views

urlpatterns = [
    path("create-real-estate-listing/", views.CreateRealEstateListing.as_view()),
    path("user-real-estate-listing/", views.UserRealEstateListingListView.as_view()),
    path("real-estate-listing/", views.UserRealEstateListingListView.as_view()),
    path("real-estate-listing/<int:pk>/detail/", views.RealEstateListingViewRetrieveView.as_view()),
    path("real-estate-listing/<int:pk>/update/", views.UpdateRealEstateListingView.as_view()),
    path("real-estate-listing/<int:pk>/delete/", views.DeleteRealEstateListingView.as_view()),
    path("add-extra-document/", views.ExtraDocumentCreateView.as_view()),
    path("extra-document/<int:pk>/delete/", views.DeleteRealEstateListingView.as_view()),
    path("add-token-detail/", views.AddTokenDetail.as_view()),
    path("token-detail/<int:pk>/delete/", views.AddTokenDetail.as_view()),
]
