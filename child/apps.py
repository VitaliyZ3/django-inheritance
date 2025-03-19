from django.apps import AppConfig


class ChildConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'child'

    def ready(self):
        from core.patcher import extend_models
        extend_models()