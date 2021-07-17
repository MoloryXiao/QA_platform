# coding: utf-8
"""
 @Topic:

 @Date: 2021-03-11

 @Author: lette.xiao

 @Copyright（C）: 2014-2021 X-Financial Inc. All rights reserved.
"""
from django.urls import path

from apps.vuetest import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'projects', views.ProjectViewSet)
urlpatterns = [
    # path('', views.index),
    path('projects/', views.ProjectsList.as_view())
]
# urlpatterns += router.urls
