from django.urls import path
from api.views.ai import enhance_summary, generate_summary

urlpatterns = [
    path("ai/enhance-summary/", enhance_summary),
    path("ai/generate-summary/", generate_summary),
]
