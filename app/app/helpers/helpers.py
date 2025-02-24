from rest_framework import serializers
from django.apps import apps
from app.models import models
from app.constants import app_constants
from app.helpers.authentication import Token

import hmac
import time
import base64
import hashlib
import struct
import base64
import random


class APIHelpers:

    def __init__(self, request):
        self.request = request

    def is_permissible(self):
        """To check whether it is permissible or not"""
        if self.request.headers.get("Authorization") != None:
            return Token().token_is_valid(
                self.request.headers.get("Authorization", "").split(" ")[1]
            )
        else:
            return False

    def get_user_from_token(self):
        """To get the token"""
        if self.request.headers.get("Authorization") != None:
            return Token().get_user(
                self.request.headers.get("Authorization", "").split(" ")[1]
            )

    def is_login_required(self):
        """A flag to check whether user is authenticated."""
        return self.request.user.is_authenticated


class OTPHelpers:

    def __init__(self):
        """An OTP Helper for OTPs, it can be used for different use cases."""
        pass

    def generate_6_digit_code(self):
        """Generate a random 6 digit number, can be used in verifications."""
        code = random.randint(0, 999999)
        return f"{code:06}"

    def to_base32(self, input_string):
        """Convert string to base 64"""
        byte_string = input_string.encode("utf-8")
        base32_encoded = base64.b32encode(byte_string)
        base32_string = base32_encoded.decode("utf-8")
        return base32_string

    def generate_numeric_totp(self, secret, interval=5):
        """Generate a random 6 digit number that is purely code timebased, can be used in verifications."""
        key = base64.b32decode(secret.upper())
        current_time = int(time.time() // interval)
        msg = struct.pack(">Q", current_time)
        hmac_hash = hmac.new(key, msg, hashlib.sha1).digest()
        offset = hmac_hash[-1] & 0x0F
        truncated_hash = hmac_hash[offset : offset + 4]
        code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
        totp = code % 1000000
        return str(totp).zfill(6)


class ModelHelpers:
    """
    A predefined for model helpers.
    predefined_models can be used to get all the models with the exemption of EXCEPT models in
    constants.
    """

    def __init__(self) -> None:
        """Can be used for models."""
        self.predefined_models = None
        self.all_models = []
        self.__initialize()

    def get_model_instance(self, model_name: str) -> models:
        """Get the model instance return the model itself."""
        try:
            return apps.get_model("app", model_name)
        except Exception as e:
            return None

    def __initialize(self) -> None:
        """Use to initialize models."""
        # Get a list of all installed models
        installed_models = apps.get_models()
        self.predefined_models = []

        for model in installed_models:
            # Get the name of the model and append it to the list
            if model.__name__ not in app_constants.EXCEPT_MODELS:
                self.all_models.append(model)
                self.predefined_models.append(model.__name__)


class SerializerHelpers:
    """A predefined for serializer helpers."""

    def __init__(self):
        pass

    def create_serializer(self, model_name: models, app_name: str) -> serializers:
        """
        Create an automatic serializer for your API that include(s) auto joining of table.
        """
        django_model = apps.get_model(app_label=str(app_name), model_name=model_name)
        # print(django_model, "Autoserializer was built.")

        class AutoSerializer(serializers.ModelSerializer):

            class Meta:
                model = django_model
                fields = "__all__"
                depth = 10  # 10 Depths of table auto joined.

        return AutoSerializer
