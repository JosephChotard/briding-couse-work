from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_page, name='cv_page'),
    path('edit/', views.cv_edit_page, name='cv_edit_page')
]
