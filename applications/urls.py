from django.urls import path

from applications import views

app_name = 'applications'

urlpatterns = [
    path('create-application/', views.create_application, name='create_application'),
]