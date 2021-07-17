from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
import json
from django.views import View
from apps.project.models import Project

from apps.vuetest.serializer import ProjectModelSerializer
from rest_framework.viewsets import ModelViewSet


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectsList(View):

    def get(self, request):
        """
        处理查询项目请求
        :param request:
        :return:
        """
        # 取出所有项目数据
        project_qs = Project.objects.all()
        # 序列化（非json转为json），当序列化内容为查询集(多个)时，需要指定many=True
        serializer = ProjectModelSerializer(instance=project_qs, many=True)
        # JsonResponse第一个参数默认只能为dict字典，若要设置为其他类型，需要将safe=False
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """
        处理新增项目请求
        :param request:
        :return:
        """
        # 从请求体获取json格式的数据
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data)
        # 反序列化（json转为非json）
        serializer = ProjectModelSerializer(data=python_data)
        # 字段校验
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            print(e)
            return JsonResponse(serializer.errors, status=400)

        project = Project.objects.create(**serializer.validated_data)
        serializer = ProjectModelSerializer(instance=project)
        return JsonResponse(serializer.data, safe=False, status=201)


def index(request):
    return render(request, "vue_test.html")

