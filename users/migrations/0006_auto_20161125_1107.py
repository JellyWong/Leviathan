# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 03:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20161125_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpublisher',
            name='id_hospital',
            field=models.ForeignKey(db_column='id_hospital', on_delete=django.db.models.deletion.CASCADE, to='users.Hospital'),
        ),
        migrations.AlterField(
            model_name='adminreceptor',
            name='id_hospital',
            field=models.ForeignKey(db_column='id_hospital', on_delete=django.db.models.deletion.CASCADE, to='users.Hospital'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id_adminreceptor',
            field=models.ForeignKey(db_column='id_adminreceptor', on_delete=django.db.models.deletion.CASCADE, to='users.Adminreceptor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id_bulletin',
            field=models.ForeignKey(db_column='id_bulletin', help_text='\u5206\u8bca\u53f0\u64cd\u4f5c\u5458\u4ece\u8fd9\u91cc\u53d6\u5f97\u9884\u7ea6\u4fe1\u606f', on_delete=django.db.models.deletion.CASCADE, to='users.Bulletin'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id_patient',
            field=models.ForeignKey(db_column='id_patient', on_delete=django.db.models.deletion.CASCADE, to='users.Patient'),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='id_adminpublisher',
            field=models.ForeignKey(db_column='id_adminpublisher', help_text='\u53d1\u5e03\u8005', on_delete=django.db.models.deletion.CASCADE, to='users.Adminpublisher'),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='id_doctor_department',
            field=models.ForeignKey(db_column='id_doctor_department', help_text='\u53ef\u9884\u7ea6\u7684\u533b\u751f', on_delete=django.db.models.deletion.CASCADE, to='users.DoctorDepartment'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id_hospital',
            field=models.ForeignKey(db_column='id_hospital', on_delete=django.db.models.deletion.CASCADE, to='users.Hospital'),
        ),
        migrations.AlterField(
            model_name='doctordepartment',
            name='id_department',
            field=models.ForeignKey(db_column='id_department', on_delete=django.db.models.deletion.CASCADE, to='users.Department'),
        ),
        migrations.AlterField(
            model_name='doctordepartment',
            name='id_doctor',
            field=models.ForeignKey(db_column='id_doctor', on_delete=django.db.models.deletion.CASCADE, to='users.Doctor'),
        ),
    ]