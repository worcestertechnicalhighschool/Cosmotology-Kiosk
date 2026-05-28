from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('feedback', views.feedback_view, name='feedback'),
    path('sign-in', views.signIn_view, name='sign-in'),
    path('welcome', views.welcome_page, name='welcome'),
    path('services', views.services_page, name='services'),
    ]