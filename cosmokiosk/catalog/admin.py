from django.contrib import admin
from django.apps import apps

class ClientAdmin(admin.ModelAdmin): # For the Client_Waiver model
    list_display = ("firstname", "lastname", "sign_date")

class QuestionAdmin(admin.ModelAdmin): # For the Feedback_Questions model
    pass

class ResponsesAdmin(admin.ModelAdmin): # For the Feedback model
    pass

class WaxingAdmin(admin.ModelAdmin): # For the Waxing_Waiver model
    pass

class ServiceAdmin(admin.ModelAdmin): # For the Services model
    pass



app_models = apps.get_app_config('catalog').get_models()
for m in app_models:
    admin.site.register(m)