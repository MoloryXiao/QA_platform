from django.db import models
from tester_home.models.project import Project


class Module(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField('模块名称', max_length=50)
    description = models.TextField('模块描述', default='')
    status = models.BooleanField('状态', default=1)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name
