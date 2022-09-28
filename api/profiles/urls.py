from django.urls import path

from .views import GetProfileAPIView, TopEmployersListAPIView, UpdateProfileAPIView

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"
    ),
    path("top-employer/all/", TopEmployersListAPIView.as_view(), name="top-agents"),
]
