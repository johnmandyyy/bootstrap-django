from django.apps import AppConfig
from app.jobs import updater

class MainConfig(AppConfig):
    name = 'app'

    def ready(self):
        updater.start()