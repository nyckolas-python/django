from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('monday/', views_week_days.monday),
    path('tuesday/', views_week_days.tuesday),
    
]