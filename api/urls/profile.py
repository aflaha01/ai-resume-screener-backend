from django.urls import path
from api.views.profile import SaveProfileView, GetSkillsView

urlpatterns = [
    path("save/", SaveProfileView.as_view(), name="profile-save"),
    path("skills/", GetSkillsView.as_view(), name="profile-skills"),
]
