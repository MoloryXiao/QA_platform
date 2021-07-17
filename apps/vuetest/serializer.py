# coding: utf-8
"""
 @Topic:

 @Date: 2021-07-15

 @Author: lette.xiao

 @Copyright（C）: 2014-2019 X-Financial_tmp Inc.   All rights reserved.

 注意：本内容仅限于小赢科技有限责任公司内部传阅，禁止外泄以及用于其他的商业目的。
"""
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.project.models import Project


class ProjectModelSerializer(serializers.Serializer):
    name = serializers.CharField(label='项目名称', max_length=200)
    description = serializers.CharField(label='描述123', allow_null=False, help_text='描述1234')

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Project
        fields = "__all__"
