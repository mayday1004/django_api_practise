from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import debug_toolbar

schema_view = get_schema_view(
    openapi.Info(
        title="Natours API",
        default_version="v1",
        description="This is a REST API for a Natours service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("tours/", include("tour.urls")),
    path("users/", include("core.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path(
        "swagger<format>.json|.yaml/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
]
