from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists_page, name='lists_page'),
]
