# coding: utf-8
"""
 @Topic:

 @Date: 2021-03-11

 @Author: lette.xiao

 @Copyright（C）: 2014-2021 X-Financial Inc. All rights reserved.
"""
from django.urls import path
from apps.project import views

urlpatterns = [
    path('', views.project_manage),
    path('project_add', views.project_add),
    path('project_modify', views.project_manage),
    path('project_modify/<int:project_id>/', views.project_modify),
    path('project_delete', views.project_manage),
    path('project_delete/<int:project_id>/', views.project_delete),
    path('search', views.project_search),
]