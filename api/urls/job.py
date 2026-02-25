from django.urls import path
from api.views.job import JobListCreateView

urlpatterns = [
    path("jobs/", JobListCreateView.as_view(), name="jobs"),
]