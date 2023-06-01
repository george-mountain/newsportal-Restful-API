from django.contrib import admin
from django.urls import path, include  # new
from drf_spectacular.views import (
    SpectacularAPIView,  # for schema
    SpectacularRedocView,  # for docs using Redoc
    SpectacularSwaggerView,  # for docs using Swagger
)  # for dynamic API documentation SCHEMA
from django.conf import settings
from django.conf.urls.static import static


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
    path(
        "api/schema/", SpectacularAPIView.as_view(), name="schema"
    ),  # endpoint for the api  schema
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),  # endpoint for the API documentation using Redocs
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),  # endpoint for the API documentation using Swagger
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
