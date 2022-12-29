from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getcredit/', views.getcredit, name='getcredit'),
    path('sendsms/', views.sendsms, name='sendsms'),
]