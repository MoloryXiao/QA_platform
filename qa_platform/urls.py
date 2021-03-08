"""qa_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tester_home.views import views_login
from tester_home.views import views_project
from tester_home.views import views_module
from tester_home.views import views_mock

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_login.login),
    path('login/', views_login.login),
    path('logout/', views_login.logout),
    path('accounts/login/', views_login.relogin),

    path('project_manage/', views_project.project_manage),
    path('project_manage/project_add', views_project.project_add),
    path('project_manage/project_modify', views_project.project_manage),
    path('project_manage/project_modify/<int:project_id>/', views_project.project_modify),
    path('project_manage/project_delete', views_project.project_manage),
    path('project_manage/project_delete/<int:project_id>/', views_project.project_delete),
    path('project_manage/search', views_project.project_search),

    path('module_manage/', views_module.module_manage),
    path('mock_manage/', views_mock.mock_manage),
    path('mock_manage/mock_add', views_mock.mock_add),
    path('mock_manage/search', views_mock.mock_search),
    path('mock_manage/mock_delete', views_mock.mock_manage),
    path('mock_manage/mock_delete/<int:mock_config_id>/', views_mock.mock_delete),
    path('mock_manage/mock_modify', views_mock.mock_manage),
    path('mock_manage/mock_modify/<int:mock_config_id>/', views_mock.mock_modify),
]