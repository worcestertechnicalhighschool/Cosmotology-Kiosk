from django.contrib import admin
#from django.contrib.admin import ModelAdmin
#from django.apps import apps
from .models import Client_Waiver




class ClientAdmin(admin.ModelAdmin): # For the Client_Waiver model
    list_display = ("first_name", "last_name", "date_time")
    list_per_page = 25

class QuestionAdmin(admin.ModelAdmin): # For the Feedback_Questions model
    list_display = ("question", "question_text") 

class ResponsesAdmin(admin.ModelAdmin): # For the Feedback model
    list_display = ("questions", "feedback_answer", "client")

class WaxingAdmin(admin.ModelAdmin): # For the Waxing_Waiver model
    pass

class ServiceAdmin(admin.ModelAdmin): # For the Services model
    pass



admin.site.register(Client_Waiver, ClientAdmin)



# models_and_admins = {
#     (Client_Waiver, ClientAdmin)
# }

# for model, admin in models_and_admins:
#         admin.site.register(model, admin)

# app_models = apps.get_app_config('catalog').get_models()
# admin_models = [ClientAdmin, QuestionAdmin, ResponsesAdmin, WaxingAdmin, ServiceAdmin]
# for m in app_models:
#     #for j in admin_models:
#         admin.site.register(m)
     
# #for j in app_models: