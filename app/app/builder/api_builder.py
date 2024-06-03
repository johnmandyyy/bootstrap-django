from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.models import *
from app.helpers.helpers import SerializerHelpers
from app.api import *
from django.db import models
from app.logs.logging import Logger
from app.constants import app_constants
from datetime import datetime
from app.helpers.authentication import Token
from rest_framework.response import Response as DjangoResponse
from django.contrib.auth import logout, authenticate, login

class APIBuilder:

    def __init__(self, model_name: str, app_name: str, model_instance: models) -> None:
        """An API Generics Builder"""

        self.model_name = model_name
        self.model = model_instance
        self.app_name = app_name
        self.list_create = None
        self.get_update_destroy = None

    def build(self, has_token = False):

        class ListCreate(ListCreateAPIView):

            queryset = self.model.objects.all()
            serializer_class = SerializerHelpers().create_serializer(
                self.model_name, self.app_name
            )
            
            def __is_permissible(self, request):
                
                if request.headers.get('Authorization') != None:
                    return Token().token_is_valid(request.headers.get('Authorization', '').split(' ')[1])
                
            def __get_user_from_token(self, request):
                if request.headers.get('Authorization') != None:
                    return Token().get_user(request.headers.get('Authorization', '').split(' ')[1])

            def get(self, request, *args, **kwargs):

                response = None
                start_time = datetime.now()

                if self.__is_permissible(request) == True:
                    response = super().get(request, *args, **kwargs)
                    if not request.user.is_authenticated:
                        login(request, self.__get_user_from_token(request))
                else:
                    logout(request)
                    response = DjangoResponse({
                        "details": "Permission Denied"
                    }, 401)

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
