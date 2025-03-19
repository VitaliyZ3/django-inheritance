from django.apps import apps
from django.db import models
import inspect
import importlib

def get_child_models():
    """Шукає всі моделі в 'child', навіть якщо вони abstract"""
    child_models = []
    module = importlib.import_module("child.models")  # Імпортуємо child.models

    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, models.Model) and hasattr(obj, "extends"):
            child_models.append(obj)

    return child_models

def extend_models():
    """Автоматично додає поля та методи з розширених моделей у батьківські"""

    parent_models = {model.__name__: model for model in apps.get_app_config('parent').get_models()}
    # child_models = [model for model in apps.get_app_config('child').get_models() if hasattr(model, 'extends')]\
    child_models = get_child_models()

    for child_model in child_models:
        parent_name = getattr(child_model, 'extends', None)

        if parent_name and parent_name in parent_models:
            parent_model = parent_models[parent_name]
            print(f"🔧 Extending {parent_name} with {child_model.__name__}")

            # Додаємо поля
            for field in child_model._meta.fields:
                if field.name != 'base' and not hasattr(parent_model, field.name):
                    field.contribute_to_class(parent_model, field.name)

            # Додаємо методи
            for attr_name in dir(child_model):
                if not attr_name.startswith('_') and not hasattr(parent_model, attr_name):
                    attr = getattr(child_model, attr_name)
                    if callable(attr):
                        setattr(parent_model, attr_name, attr)