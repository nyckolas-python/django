from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('<day_name>/', views_week_days.get_day_name),
    
]