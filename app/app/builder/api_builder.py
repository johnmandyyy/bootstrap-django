from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from app.models import *
from app.helpers.helpers import SerializerHelpers
from app.api import *
from django.db import models
from app.logs.logging import Logger
from app.constants import app_constants
from django.contrib.auth import logout, login
from app.constants import response_constants as PREDEFINED_RESPONSE
from app.helpers.helpers import APIHelpers
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import FieldError


class APIBuilder:

    def __init__(self, model_name: str, app_name: str, model_instance: models) -> None:
        """An API Generics Builder"""

        self.model_name = model_name
        self.model = model_instance
        self.app_name = app_name

        self.list_create = None
        self.list_get = None
        self.get_update_destroy = None

    def filter_model(self):
        """A method used for subclass to return instance model for subclass as property of APIBuilder"""
        return self.model

    def build(self, has_token=False):

        class ListGet(ListAPIView):

            queryset = self.filter_model().objects.all()
            serializer_class = SerializerHelpers().create_serializer(
                self.model_name, self.app_name
            )

            pagination_class = None

            def get(self, request):
                """
                Example usage in ENDPOINT:
                ?page=1&id=63
                is equivalent to models.objects.all().filter(id = 63)
                """

                querydict = request.GET

                # for key, value in querydict.items():
                if "page" in querydict:
                    self.pagination_class = PageNumberPagination

                filters = {
                    key: value for key, value in querydict.items() if key != "page"
                }

                try:
                    self.queryset = self.queryset.model.objects.all().filter(**filters)
                    return super().get(request)
                except FieldError:
                    return PREDEFINED_RESPONSE.INVALID_REQUEST

        class ListCreate(ListCreateAPIView):

            queryset = self.model.objects.all()
            serializer_class = SerializerHelpers().create_serializer(
                self.model_name, self.app_name
            )

            def get(self, request, *args, **kwargs):

                if has_token == True:

                    if APIHelpers(
                        request
                    ).is_permissible():  # To check if token is still valid.

                        if (
                            not request.user.is_authenticated
                        ):  # Login if not yet logged in using token.
                            login(request, APIHelpers(request).get_user_from_token())

                    else:

                        if request.user.is_authenticated:
                            logout(request)

                        response = PREDEFINED_RESPONSE.PERMMISSION_DENIED

                        Logger(
                            message="POST Endpoint / Executed",
                            source=__name__,
                            request=request,
                            level=app_constants.LOG_LEVEL.INFO,
                            log_type=app_constants.LOG_TYPE.HTTP_REQUEST,
                            response_status=response.status_code,
                        )

                        return response

                response = super().get(request, *args, **kwargs)

                Logger(
                    message="POST Endpoint / Executed",
                    source=__name__,
                    request=request,
                    level=app_constants.LOG_LEVEL.INFO,
                    log_type=app_constants.LOG_TYPE.HTTP_REQUEST,
                    response_status=response.status_code,
                )

                return response

            def post(self, request, *args, **kwargs):

                response = super().post(request, *args, **kwargs)

                Logger(
                    message="POST Endpoint / Executed",
                    source=__name__,
                    request=request,
                    level=app_constants.LOG_LEVEL.INFO,
                    log_type=app_constants.LOG_TYPE.HTTP_REQUEST,
                    response_status=None,
                )

                return response

        class GetUpdateDestroy(RetrieveUpdateDestroyAPIView):

            queryset = self.model.objects.all()
            serializer_class = SerializerHelpers().create_serializer(
                self.model_name, self.app_name
            )
            lookup_field = "pk"

        self.list_create = ListCreate()
        self.get_update_destroy = GetUpdateDestroy()
        self.list_get = ListGet()

        return self
