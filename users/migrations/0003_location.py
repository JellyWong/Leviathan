# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161122_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id_location', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('province', models.CharField(help_text='\u7701/\u81ea\u6cbb\u533a(\u76f4\u8f96\u5e02\u548c\u7279\u522b\u884c\u653f\u533a\u7559\u767d', max_length=20, null=True)),
                ('city', models.CharField(help_text='\u5e02', max_length=20)),
                ('county', models.CharField(help_text='\u4e3b\u57ce\u533a/\u53bf', max_length=20)),
                ('street', models.CharField(help_text='\u8857\u9053\u5730\u5740\u95e8\u724c\u53f7', max_length=50, null=True)),
            ],
            options={
                'db_table': 'location',
            },
        ),
    ]
