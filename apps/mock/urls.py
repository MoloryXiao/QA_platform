# coding: utf-8
"""
 @Topic:

 @Date: 2021-03-11

 @Author: lette.xiao

 @Copyright（C）: 2014-2019 X-Financial_tmp Inc.   All rights reserved.

 注意：本内容仅限于小赢科技有限责任公司内部传阅，禁止外泄以及用于其他的商业目的。
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