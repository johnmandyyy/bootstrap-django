from app.helpers.helpers import ModelHelpers
from django.urls import path
from app.builder.api_builder import APIBuilder
from app.constants import app_constants
from app.models import RouteExclusion
from app.logs.logging import Logger
from datetime import datetime

class UrlPatternBuilder:

    def __init__(self):
        """A URL Pattern builder for Generics API"""
        self.list_create_patterns = []
        self.retrieve_update_delete_patterns = []
        self.__combined_list = []

    def __validate(self):
        """To validate all the models if it is
        still existing so that the endpoints route will be updated"""

        result = RouteExclusion.objects.all()
        if len(result) > 0:
            for url in result:
                if url.route not in self.__combined_list:
                    RouteExclusion.objects.all().filter(route=url.route).delete()

    def __list_create_endpoint_state(self, list_create_url):
        """A method for validating a list create endpoint to be appended and returns the state."""

        self.__combined_list.append(list_create_url)

        result = RouteExclusion.objects.all().filter(route=str(list_create_url))
        if len(result) < 1:
            RouteExclusion.objects.create(route=str(list_create_url))

        result = RouteExclusion.objects.all().filter(route=str(list_create_url))
        if len(result) > 0:
            for filtered in result:
                return filtered

    def __retrieve_update_delete_state(self, retrieve_update_delete_url):

        self.__combined_list.append(retrieve_update_delete_url)

        result = RouteExclusion.objects.all().filter(
            route=str(retrieve_update_delete_url)
        )
        if len(result) < 1:
            RouteExclusion.objects.create(route=str(retrieve_update_delete_url))

        result = RouteExclusion.objects.all().filter(
            route=str(retrieve_update_delete_url)
        )
        if len(result) > 0:
            for filtered in result:
                return filtered
            
    def __generic_specs(self, list_create_state, retrieve_update_state):
        pass

    def build(self, name=app_constants.APP_NAME):
        """A method used to build the URL Pattern"""
        django_models = ModelHelpers()
        for each_models in django_models.predefined_models:

            model_url_name = each_models.lower()

            list_create_url = f"list-create/{model_url_name}/"
            get_update_destroy_url = f"get-update-destroy/{model_url_name}/<int:pk>/"

            LIST_CREATE_STATE = self.__list_create_endpoint_state(list_create_url)
            RETRIEVE_UPDATE_DELETE_STATE = self.__retrieve_update_delete_state(get_update_destroy_url)
            
            if LIST_CREATE_STATE.is_enabled == True:

                LIST_CREATE_INSTANCE = APIBuilder(
                    each_models, name, ModelHelpers().get_model_instance(each_models)
                )

                LIST_CREATE_INSTANCE.build(has_token = LIST_CREATE_STATE.required_token)
                
                self.list_create_patterns.append(
                    path(
                        list_create_url,
                        LIST_CREATE_INSTANCE.list_create.as_view(),
                        name="list-create" + "-" + model_url_name,
                    )
                )

            if RETRIEVE_UPDATE_DELETE_STATE.is_enabled == True:

                RETRIEVE_UPDATE_DELETE_INSTANCE = APIBuilder(
                    each_models, name, ModelHelpers().get_model_instance(each_models)
                )

                RETRIEVE_UPDATE_DELETE_INSTANCE.build(has_token = RETRIEVE_UPDATE_DELETE_STATE.required_token)

                self.retrieve_update_delete_patterns.append(
                    path(
                        get_update_destroy_url,
                        RETRIEVE_UPDATE_DELETE_INSTANCE.get_update_destroy.as_view(),
                        name="get-update-delete-categories" + "-" + model_url_name,
                    )
                )
        else:
            self.__validate()