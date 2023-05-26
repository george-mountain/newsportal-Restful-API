from django.contrib import admin
from django.urls import path, include  # new


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("posts.urls")),  # new
    path("api-auth/", include("rest_framework.urls")),  # new needed for authorization
    path(
        "api/v1/dj-rest-auth/", include("dj_rest_auth.urls")
    ),  # new endpoints for signin, password reset, confirm
    path(
        "api/v1/dj-rest-auth/registration/",  # new
        include("dj_rest_auth.registration.urls"),
    ),
]
