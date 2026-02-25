from django.urls import path, include

urlpatterns = [
    path("user/", include("api.urls.user")),
    path("auth/", include("api.urls.authentication")),
    path("resume/", include("api.urls.resume")),
    path("", include("api.urls.profile")),
    path("", include("api.urls.ai")),
    path("", include("api.urls.hr_profile")),
    path("", include("api.urls.job")),
]
