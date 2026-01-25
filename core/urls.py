from django.contrib import admin
from django.urls import path

from apps.evaluations.views import AboutUsView, DashboardView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", DashboardView.as_view(), name="dashboard"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
]
