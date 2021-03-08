from django.db import models


class MockConfig(models.Model):
    business_name = models.CharField(verbose_name='业务名称', max_length=50, null=False)
    business_tag = models.CharField(verbose_name='业务标识', max_length=50, null=False)
    message_format = models.SmallIntegerField(verbose_name='报文格式 1:json 2:xml 3:form', default=0, null=False)
    mock_type = models.SmallIntegerField(verbose_name='Mock匹配方式 1:完整链接匹配 2:请求报文参数匹配', default=0, null=False)
    mock_match_field = models.CharField(verbose_name='接口匹配字段', max_length=50, default='', null=True)
    is_diff_merchant = models.SmallIntegerField(verbose_name='是否区分商户号 0:否 1:是', default=0, null=False)
    merchant_field = models.CharField(verbose_name='商户号取值字段', max_length=50, default='', null=True)

    status = models.SmallIntegerField(verbose_name='状态', default=1)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.business_name
