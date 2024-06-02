from django.contrib import admin
from app.models import *
from app.helpers.helpers import ModelHelpers

MODELS = ModelHelpers()
if len(MODELS.predefined_models) > 0:
    for each_models in MODELS.predefined_models:
        admin.site.register(
            MODELS.get_model_instance(each_models)
        )

