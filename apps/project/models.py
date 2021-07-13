from django.db import models


class Project(models.Model):
    name = models.CharField(db_column='FstrProjectName', verbose_name='项目名称', max_length=50)
    description = models.TextField(db_column='FstrDescription', verbose_name='项目描述', default='')
    status = models.BooleanField(db_column='FuiStatus', verbose_name='状态', default=1)
    create_time = models.DateTimeField(db_column='FuiCreateTime', verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(db_column='FuiUpdateTime', verbose_name='更新时间', auto_now=True)

    class Meta:
        db_table = 't_project'

    def __str__(self):
        return self.name