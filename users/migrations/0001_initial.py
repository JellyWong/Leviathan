# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminpublisher',
            fields=[
                ('id_adminpublisher', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('loginname', models.CharField(help_text='\u767b\u9646\u6807\u8bc6\u7b26\uff0c\u5b9e\u9645\u53ef\u4e3a\u81ea\u5b9a\u4e49\u7528\u6237\u540d\u6216\u88ab\u6ce8\u518c\u53d7\u7406\u65b9\u7ed9\u5b9a\u7684\u7528\u6237\u540d', max_length=45, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('telephone', models.CharField(blank=True, help_text='\u6216\u8bb8\u7528\u4e8e\u5907\u6848\u5b58\u6863\u7684\u4fe1\u606f', max_length=15, null=True)),
                ('email', models.EmailField(blank=True, help_text='\u9009\u586b\uff0c\u7528\u4e8e\u5907\u6848', max_length=50, null=True)),
                ('createtime', models.DateTimeField(blank=True, help_text='\u6ce8\u518c\u4e8b\u4ef6', null=True)),
            ],
            options={
                'db_table': 'adminpublisher',
            },
        ),
        migrations.CreateModel(
            name='Adminreceptor',
            fields=[
                ('id_adminreceptor', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('loginname', models.CharField(help_text='\u767b\u9646\u6807\u8bc6\u7b26\uff0c\u5b9e\u9645\u53ef\u4e3a\u81ea\u5b9a\u4e49\u7528\u6237\u540d\u6216\u9662\u65b9\u5b9a\u4e49\u7684\u7528\u6237\u540d(\u6bd4\u5982\u5de5\u53f7)', max_length=45, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('createtime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'adminreceptor',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id_appointment', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('ispaid', models.BooleanField(default='0')),
                ('registrationtime', models.DateTimeField(blank=True, help_text='\u5230\u9662\u53d6\u53f7\u65f6\u95f4-\u6b64\u9879\u8bf4\u660e\u4e86\u662f\u5426\u723d\u7ea6', null=True)),
                ('createtime', models.DateTimeField(help_text='\u9884\u7ea6\u5355\u751f\u6210\u65f6\u95f4')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id_bulletin', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('availabletime', models.DateTimeField(help_text='\u53ef\u9884\u7ea6\u65f6\u95f4\u6bb5')),
                ('fee', models.FloatField(default=0, help_text='(\u9884\u7ea6)\u6302\u53f7\u8d39')),
                ('countavailable', models.IntegerField(help_text='\u521d\u59cb\u58f0\u660e\u7684\u53ef\u9884\u7ea6\u6570\u91cf')),
                ('countoccupied', models.IntegerField(help_text='\u5df2\u9884\u7ea6\u6570\u91cf')),
                ('createtime', models.DateTimeField(blank=True, help_text='\u6700\u540e\u4e00\u6b21\u65b0\u589e\u9884\u7ea6\u8bb0\u5f55\u7684\u65f6\u95f4', null=True)),
                ('id_adminpublisher', models.ForeignKey(db_column='id_adminpublisher', help_text='\u53d1\u5e03\u8005', on_delete=django.db.models.deletion.CASCADE, to='users.Adminpublisher')),
            ],
            options={
                'db_table': 'bulletin',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id_department', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('information', models.TextField(blank=True, help_text='\u6982\u8ff0', null=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id_doctor', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='\u533b\u751f\u5b9e\u540d', max_length=45)),
                ('level', models.CharField(choices=[('\u4e3b\u4efb\u533b\u5e08', '\u4e3b\u4efb\u533b\u5e08'), ('\u526f\u4e3b\u4efb\u533b\u5e08', '\u526f\u4e3b\u4efb\u533b\u5e08'), ('\u4e3b\u6cbb\u533b\u5e08', '\u4e3b\u6cbb\u533b\u5e08'), ('\u4f4f\u9662\u533b\u5e08', '\u4f4f\u9662\u533b\u5e08')], max_length=10)),
                ('information', models.TextField(blank=True, null=True)),
                ('picture', models.CharField(blank=True, help_text='\u533b\u751f\u7167\u7247\uff0c\u5b58\u8def\u5f84', max_length=90, null=True)),
                ('speciality', models.CharField(blank=True, help_text='\u4e3b\u6cbb\u7279\u957f', max_length=90, null=True)),
                ('careertime', models.IntegerField(default=0, help_text='\u533b\u9f84\uff0c\u5355\u4f4d\u4e3a\u5e74')),
                ('gender', models.CharField(choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('createtime', models.DateTimeField(blank=True, help_text='\u751f\u6210\u65f6\u95f4', null=True)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='DoctorDepartment',
            fields=[
                ('id_doctor_department', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('id_department', models.ForeignKey(db_column='id_department', on_delete=django.db.models.deletion.CASCADE, to='users.Department')),
                ('id_doctor', models.ForeignKey(db_column='id_doctor', on_delete=django.db.models.deletion.CASCADE, to='users.Doctor')),
            ],
            options={
                'db_table': 'doctor_department',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id_hospital', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('level', models.CharField(choices=[('\u4e00\u7ea7\u4e19\u7b49', '\u4e00\u7ea7\u4e19\u7b49'), ('\u4e00\u7ea7\u4e59\u7b49', '\u4e00\u7ea7\u4e59\u7b49'), ('\u4e00\u7ea7\u7532\u7b49', '\u4e00\u7ea7\u7532\u7b49'), ('\u4e8c\u7ea7\u4e19\u7b49', '\u4e8c\u7ea7\u4e19\u7b49'), ('\u4e8c\u7ea7\u4e59\u7b49', '\u4e8c\u7ea7\u4e59\u7b49'), ('\u4e8c\u7ea7\u7532\u7b49', '\u4e8c\u7ea7\u7532\u7b49'), ('\u4e09\u7ea7\u4e19\u7b49', '\u4e09\u7ea7\u4e19\u7b49'), ('\u4e09\u7ea7\u4e59\u7b49', '\u4e09\u7ea7\u4e59\u7b49'), ('\u4e09\u7ea7\u7532\u7b49', '\u4e09\u7ea7\u7532\u7b49'), ('\u4e09\u7ea7\u7279\u7b49', '\u4e09\u7ea7\u7279\u7b49')], max_length=20)),
                ('type', models.CharField(blank=True, choices=[('\u666e\u901a', '\u666e\u901a'), ('\u4e13\u79d1', '\u4e13\u79d1')], default='\u666e\u901a', help_text='\u533b\u7597\u670d\u52a1\u662f\u5426\u4e13\u79d1', max_length=20, null=True)),
                ('information', models.TextField(blank=True, default='\u65e0\u8bf4\u660e\u4fe1\u606f')),
                ('telephone', models.CharField(blank=True, max_length=15, null=True)),
                ('picture', models.CharField(blank=True, help_text='\u533b\u9662\u7167\u7247\uff0c\u5b58\u8def\u5f84', max_length=90, null=True)),
                ('createtime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hospital',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id_location', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('province', models.CharField(blank=True, help_text='\u7701/\u81ea\u6cbb\u533a(\u76f4\u8f96\u5e02\u548c\u7279\u522b\u884c\u653f\u533a\u7559\u767d', max_length=20, null=True)),
                ('city', models.CharField(help_text='\u5e02', max_length=20)),
                ('county', models.CharField(help_text='\u4e3b\u57ce\u533a/\u53bf', max_length=20)),
                ('street', models.CharField(blank=True, help_text='\u8857\u9053\u5730\u5740\u95e8\u724c\u53f7', max_length=50, null=True)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id_patient', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('username', models.CharField(help_text='\u7528\u6237\u540d\uff0c\u7528\u4e8e\u767b\u9646', max_length=15, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('telephone', models.CharField(blank=True, help_text='\u9009\u586b\uff0c\u7528\u4e8e\u5907\u6848', max_length=15)),
                ('email', models.EmailField(blank=True, help_text='\u9009\u586b\uff0c\u7528\u4e8e\u5907\u6848', max_length=50)),
                ('name', models.CharField(help_text='\u8ba4\u8bc1\u5b9e\u540d', max_length=45)),
                ('credit', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('X', 'X')], help_text='\u4fe1\u7528\u989d\u5ea6', max_length=1)),
                ('idcardnumber', models.CharField(help_text='\u8eab\u4efd\u8bc1\u53f7\u5b9a\u957f18\u4f4d', max_length=18, unique=True)),
                ('gender', models.CharField(choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')], max_length=1)),
                ('age', models.IntegerField(default=0)),
                ('createtime', models.DateTimeField(blank=True, help_text='\u6ce8\u518c\u65f6\u95f4', max_length=100, null=True)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.AddField(
            model_name='hospital',
            name='id_location',
            field=models.ForeignKey(db_column='id_location', on_delete=django.db.models.deletion.CASCADE, to='users.Location'),
        ),
        migrations.AddField(
            model_name='department',
            name='id_hospital',
            field=models.ForeignKey(db_column='id_hospital', on_delete=django.db.models.deletion.CASCADE, to='users.Hospital'),
        ),
        migrations.AddField(
            model_name='bulletin',
            name='id_doctor_department',
            field=models.ForeignKey(db_column='id_doctor_department', help_text='\u53ef\u9884\u7ea6\u7684\u533b\u751f', on_delete=django.db.models.deletion.CASCADE, to='users.DoctorDepartment'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='id_bulletin',
            field=models.ForeignKey(db_column='id_bulletin', help_text='\u5206\u8bca\u53f0\u64cd\u4f5c\u5458\u4ece\u8fd9\u91cc\u53d6\u5f97\u9884\u7ea6\u4fe1\u606f', on_delete=django.db.models.deletion.CASCADE, to='users.Bulletin'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='id_patient',
            field=models.ForeignKey(db_column='id_patient', on_delete=django.db.models.deletion.CASCADE, to='users.Patient'),
        ),
        migrations.AddField(
            model_name='adminreceptor',
            name='id_hospital',
            field=models.ForeignKey(db_column='id_hospital', on_delete=django.db.models.deletion.CASCADE, to='users.Hospital'),
        ),
        migrations.AddField(
            model_name='adminpublisher',
            name='id_hospital',
            field=models.ForeignKey(db_column='id_hospital', on_delete=django.db.models.deletion.CASCADE, to='users.Hospital'),
        ),
    ]
