from django.contrib import admin
from django.urls import path, include  # new
from drf_spectacular.views import (
    SpectacularAPIView,  # for schema
    SpectacularRedocView,  # for docs using Redoc
    SpectacularSwaggerView,  # for docs using Swagger
)  # for dynamic API documentation SCHEMA
from dj_rest_auth.views import PasswordResetConfirmView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("posts.urls")),  # new
    path("api-auth/", include("rest_framework.urls")),  # new needed for authorization
    path(
        "api/v1/accounts/", include("dj_rest_auth.urls")
    ),  # new endpoints for signin, password reset, confirm
    path(
        "api/v1/accounts/registration/",  # new
        include("dj_rest_auth.registration.urls"),
    ),
    path(
        "api/v1/accounts/password/reset/confirm/<str:uidb64>/<str:token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
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
