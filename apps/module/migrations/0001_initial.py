# Generated by Django 3.1.6 on 2021-03-13 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='FstrModuleName', max_length=50, verbose_name='模块名称')),
                ('description', models.TextField(db_column='FstrDescription', default='', verbose_name='模块描述')),
                ('status', models.BooleanField(db_column='FuiStatus', default=1, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='FuiCreateTime', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='FuiUpdateTime', verbose_name='更新时间')),
                ('project', models.ForeignKey(db_column='FuiProjectId', on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'db_table': 't_module',
            },
        ),
    ]
