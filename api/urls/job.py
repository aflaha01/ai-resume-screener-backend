from django.urls import path
from api.views.job import JobListCreateView
from api.views.job_match import MatchedJobsView

urlpatterns = [
    path("jobs/", JobListCreateView.as_view(), name="jobs"),
    path("jobs/matched/", MatchedJobsView.as_view(), name="matched-jobs"),
]