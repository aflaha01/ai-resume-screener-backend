from django.urls import path
from api.views.hr_profile import create_hr_profile, get_hr_profile

urlpatterns = [
    path("hr/profile/", create_hr_profile),
    path("hr/profile/me/", get_hr_profile),
]
