from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('growbusiness/', views.growbusiness, name='growbusiness'), 
    path('gbfunctions/', views.gbfunctions, name = 'gbfunctions'),
    path('sentimentanalysis/', views.sentimentanalysis, name='sentimentanalysis'),
    path('sfunctions/', views.sfunctions, name='sfunctions'), 
    path('comparativeanalysis/', views.comparativeanalysis, name='comparativeanalysis'),
    path('cfunctions/', views.cfunctions, name = "cfunctions"),
    path('topbusiness/', views.topbusiness, name='topbusiness'),
    path('tbfunctions/', views.tbfunctions, name='tbfunctions'),
    path('trends/', views.trends, name='trends'),
    path('visualize/', views.visualize, name = 'visualize'),
    path('vfunctions/', views.vfunctions, name = 'vfunctions'),
    path('allfunctions/', views.allfunctions, name='allfunctions'),
]
