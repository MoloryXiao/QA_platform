# coding: utf-8
"""
 @Topic:

 @Date: 2021-03-11

 @Author: lette.xiao

 @Copyright（C）: 2014-2019 X-Financial_tmp Inc.   All rights reserved.

 注意：本内容仅限于小赢科技有限责任公司内部传阅，禁止外泄以及用于其他的商业目的。
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