from django.urls import path
from .views import create_robot, export_weekly_summary, create_robot_form, weekly_summary_view

urlpatterns = [
    path('api/robots/', create_robot, name='create_robot'),
    path('create-robot/', create_robot_form, name='create_robot_form'),
    path('api/weekly-summary/', export_weekly_summary, name='weekly_summary'),
    path('weekly-summary-page/', weekly_summary_view, name='weekly_summary_page'),

]
