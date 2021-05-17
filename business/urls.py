from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('growbusiness/', views.growbusiness, name='growbusiness'), 
    path('gbfunctions/', views.gbfunctions, name = 'gbfunctions'),
    path('sentimentanalysis/', views.sentimentanalysis, name='sentimentanalysis'), 
    path('comparativeanalysis', views.comparativeanalysis, name='comparativeanalysis'),
    path('topbusiness/', views.sentimentanalysis, name='topbusiness'),
    path('trends/', views.trends, name='trends'),

]
