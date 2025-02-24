"""
Definition of urls for app.
"""

from django.urls import path, include
from django.contrib import admin
from app.views import TemplateView
from .api import *
import app.constants.url_constants as URLConstants
from app.constants import app_constants
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView as TV

MainView = TemplateView()

list_create_patterns = URLConstants.GenericAPI.list_create_patterns
list_get_patterns = URLConstants.GenericAPI.list_get_patterns
get_update_destroy_patterns = URLConstants.GenericAPI.retrieve_update_delete_patterns


api_patterns = [
    # DOCUMENTATION
    path(
        "api_schema/",
        get_schema_view(title="API Schema", description="Guide for the REST API"),
        name="api_schema",
    ),
    path(
        "docs/",
        TV.as_view(
            template_name="app/docs.html", extra_context={"schema_url": "api_schema"}
        ),
        name="swagger-ui",
    ),
    path("api/", include((list_get_patterns, app_constants.APP_NAME))),
    path("api/", include((list_create_patterns, app_constants.APP_NAME))),
    path("api/", include((get_update_destroy_patterns, app_constants.APP_NAME))),
    path("api/login/", Login.as_view(), name="authenticate_user"),
]

template_patterns = [
    path("home/", MainView.home, name="home"),
    path("datasets/", MainView.datasets, name="datasets"),
    path("library/", MainView.library, name="library"),
    path("credibility/", MainView.credibility, name="credibility"),
    path("admin/", admin.site.urls),
    path("logout/", MainView.user_logout, name="logout"),
    path("login/", MainView.login, name="login"),
]

urlpatterns = template_patterns + api_patterns
