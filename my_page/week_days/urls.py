from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('<int:day>/', views_week_days.get_day_by_number),
    path('<str:day>/', views_week_days.get_day_name),
    
    
]