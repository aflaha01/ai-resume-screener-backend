from django.urls import path
from api.views.profile import SaveProfileView

urlpatterns = [
    path("save/", SaveProfileView.as_view(), name="save-profile"),
]
