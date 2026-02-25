from django.urls import path
from api.views.user import me, complete_onboarding

urlpatterns = [
    path("me/", me, name="user-me"),
    path("me/complete-onboarding/", complete_onboarding, name="complete-onboarding"),
]
