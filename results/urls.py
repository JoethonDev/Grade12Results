from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('bot', views.bot_result),
    path('<str:id>', views.result),
]
