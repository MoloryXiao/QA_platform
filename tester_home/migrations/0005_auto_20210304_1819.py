# Generated by Django 3.1.6 on 2021-03-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester_home', '0004_auto_20210304_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mockconfig',
            name='mock_type',
            field=models.SmallIntegerField(default=0, verbose_name='Mock匹配方式 1:完整链接匹配 2:请求报文参数匹配'),
        ),
    ]
