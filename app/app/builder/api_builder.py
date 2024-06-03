from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import *
from app.helpers.helpers import SerializerHelpers
from app.api import *
from django.db import models
from app.logs.logging import Logger
from app.constants import app_constants
from datetime import datetime

class APIBuilder:

    def __init__(self, model_name: str, app_name: str, model_instance: models) -> None:
        """An API Generics Builder"""

        self.model_name = model_name
        self.model = model_instance
        self.app_name = app_name
        self.list_create = None
        self.get_update_destroy = None

    def build(self):

        class ListCreate(ListCreateAPIView):

            queryset = self.model.objects.all()
            serializer_class = SerializerHelpers().create_serializer(
                self.model_name, self.app_name
            )
            
            def get(self, request, *args, **kwargs):
                start_time = datetime.now()
                response = super().get(request, *args, **kwargs)
                Logger(
                    message="GET Endpoint / Executed",
                    source=__name__,
                    request=request,
                    level=app_constants.LOG_LEVEL.INFO,
                    log_type=app_constants.LOG_TYPE.HTTP_REQUEST,
                    response_status = response.status_code,
                    response_data = {},
                    exec_time = str(datetime.now() - start_time)
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
                    response_status= None,
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

        return self
