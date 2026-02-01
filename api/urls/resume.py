from django.urls import path
from api.views.resume import upload_resume

urlpatterns = [
    path("upload/", upload_resume),
]
