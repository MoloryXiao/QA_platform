# coding: utf-8
"""
 @Topic:

 @Date: 2021-03-11

 @Author: lette.xiao

 @Copyright（C）: 2014-2021 X-Financial Inc. All rights reserved.
"""
from django.urls import path
from apps.mock import views

urlpatterns = [
    path('', views.mock_manage),
    path('mock_add', views.mock_add),
    path('search', views.mock_search),
    path('mock_delete', views.mock_manage),
    path('mock_delete/<int:mock_config_id>/', views.mock_delete),
    path('mock_modify', views.mock_manage),
    path('mock_modify/<int:mock_config_id>/', views.mock_modify),
]