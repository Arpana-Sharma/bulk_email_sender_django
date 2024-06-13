from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_emails, name='send_email'),
    path('', views.send_emails, name='send_email'),
]
