from django.urls import path, admin
from . import views
from django.urls import include 
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path(''. RedirectView.as_view(url='catalog/', permanent=True)),
        # handles path('feedback/', views.feedback_view, name='feedback' )
    ]