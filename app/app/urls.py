"""
Definition of urls for app.
"""

from django.urls import path, include
from django.contrib import admin
from app.views import TemplateView
from .api import *
import app.constants.url_constants as URLConstants
from app.constants import app_constants

MainView = TemplateView()

list_create_patterns = URLConstants.GenericAPI.list_create_patterns
get_update_destroy_patterns = URLConstants.GenericAPI.retrieve_update_delete_patterns

api_patterns = [
    path("api/", include((list_create_patterns, app_constants.APP_NAME))),
    path("api/", include((get_update_destroy_patterns, app_constants.APP_NAME))),
    path("api/login/", Login.as_view(), name = 'authenticate_user')
]

template_patterns = [
    path("home/", MainView.home, name="home"),
    path("datasets/", MainView.datasets, name="datasets"),
    path("library/", MainView.library, name="library"),
    path("credibility/", MainView.credibility, name="credibility"),
    path("admin/", admin.site.urls),
    path("logout/", MainView.user_logout, name="logout"),
    path("login/", MainView.login, name="login")
]

urlpatterns = template_patterns + api_patterns