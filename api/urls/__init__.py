from django.urls import path, include

urlpatterns = [
    path("auth/", include("api.urls.authentication")),
    path("resume/", include("api.urls.resume")),
    path("", include("api.urls.profile")),
    path("", include("api.urls.ai")),
]
