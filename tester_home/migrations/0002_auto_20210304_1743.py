# Generated by Django 3.1.6 on 2021-03-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester_home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mockconfig',
            old_name='business_tip',
            new_name='business_tag',
        ),
        migrations.AlterField(
            model_name='mockconfig',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name='状态'),
        ),
    ]