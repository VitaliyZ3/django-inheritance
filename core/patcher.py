import inspect
import importlib
from django.apps import apps
from django.db import models


def get_child_models(app_name: str):
    """
    Search add models from @child django application
    """
    models_app_name = f"{app_name}.models"
    child_models = []
    module = importlib.import_module(models_app_name)

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, models.Model) and hasattr(obj, "extends"):
            child_models.append(obj)

    return child_models

def extend_models(app_name):
    """
    Add modelds from @child package with inherit arrt to the application
    """
    
    # Get parents and child models
    parent_models = {model.__name__: model for model in apps.get_app_config('parent').get_models()}
    child_models = get_child_models(app_name)

    for child_model in child_models:
        # Map child models to parents
        parent_name = getattr(child_model, 'extends', None)

        # Add fields and methods from child models to parents
        if parent_name and parent_name in parent_models:
            parent_model = parent_models[parent_name]

            # Adding fields
            for field in child_model._meta.fields:
                if field.name != 'base' and not hasattr(parent_model, field.name):
                    field.contribute_to_class(parent_model, field.name)

            # Adding methods
            for attr_name in dir(child_model):
                if not attr_name.startswith('_') and not hasattr(parent_model, attr_name):
                    attr = getattr(child_model, attr_name)
                    if callable(attr):
                        setattr(parent_model, attr_name, attr)