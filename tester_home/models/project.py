from django.db import models



class Project(models.Model):
    name = models.CharField('项目名称', max_length=50)
    description = models.TextField('项目描述', default='')
    status = models.BooleanField('状态', default=1)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.name