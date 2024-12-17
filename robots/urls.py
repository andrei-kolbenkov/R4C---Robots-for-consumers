from django.urls import path
from .views import create_robot, export_weekly_summary

urlpatterns = [
    path('api/robots/', create_robot, name='create_robot'),
    path('api/weekly-summary/', export_weekly_summary, name='weekly_summary'),
]
