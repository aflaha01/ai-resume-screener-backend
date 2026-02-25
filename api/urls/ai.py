from django.urls import path
from api.views.ai import enhance_summary, generate_summary, generate_job_description

urlpatterns = [
    path("ai/enhance-summary/", enhance_summary),
    path("ai/generate-summary/", generate_summary),
    path("ai/generate-job-description/", generate_job_description),
]
