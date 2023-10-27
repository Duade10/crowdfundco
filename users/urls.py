from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="user-register"),
    path("login/", views.UserLoginView.as_view(), name="user-login"),
    path("logout/", views.UserLogoutView.as_view(), name="user-logout"),
    path("update/", views.UserUpdateView.as_view(), name="user-update"),
    path("detail/", views.UserDetailView.as_view(), name="user-detail"),
    path("delete/", views.UserDeleteView.as_view(), name="user-delete"),
]
