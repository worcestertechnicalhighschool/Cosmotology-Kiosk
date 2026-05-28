from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback_view, name='Client-Feedback'),
    path('signIn/', views.signIn_view, name='signIn'),
    path('welcome/', views.welcome_page, name='welcome')
    ]