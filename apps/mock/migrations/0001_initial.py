# Generated by Django 3.0.6 on 2021-07-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MockConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(db_column='FstrBusinessName', max_length=50, verbose_name='业务名称')),
                ('business_tag', models.CharField(db_column='FstrBusinessTag', max_length=50, verbose_name='业务标识')),
                ('message_format', models.SmallIntegerField(db_column='FuiMessageFormat', default=0, verbose_name='报文格式 1:json 2:xml 3:form')),
                ('mock_type', models.SmallIntegerField(db_column='FuiMockType', default=0, verbose_name='Mock匹配方式 1:完整链接匹配 2:请求报文参数匹配')),
                ('mock_match_field', models.CharField(db_column='FstrMockMatchField', default='', max_length=50, null=True, verbose_name='接口匹配字段')),
                ('is_diff_merchant', models.SmallIntegerField(db_column='FuiIsDiffMerchant', default=0, verbose_name='是否区分商户号 0:否 1:是')),
                ('merchant_field', models.CharField(db_column='FstrMerchantField', default='', max_length=50, null=True, verbose_name='商户号取值字段')),
                ('status', models.SmallIntegerField(db_column='FuiStatus', default=1, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='FuiCreateTime', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='FuiUpdateTime', verbose_name='更新时间')),
            ],
            options={
                'db_table': 't_mock_config',
            },
        ),
        migrations.CreateModel(
            name='ViewerIp',
            fields=[
                ('FuiId', models.AutoField(primary_key=True, serialize=False)),
                ('user_ip', models.CharField(db_column='FuiUserIp', max_length=64)),
                ('views_count', models.IntegerField(db_column='FuiViewsCount')),
                ('create_time', models.DateTimeField(db_column='FuiCreateTime')),
            ],
            options={
                'db_table': 't_view_ip',
            },
        ),
    ]
