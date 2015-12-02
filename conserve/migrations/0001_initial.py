# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prescribed_unit', models.IntegerField()),
                ('alert_unit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200)),
                ('mob', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('bill_no', models.IntegerField(default=0)),
            ],
        ),
    ]
