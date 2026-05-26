from django.contrib import admin
from django.apps import apps
app_models = apps.get_app_config('catalog').get_models()
for m in app_models:
    admin.site.register(m)