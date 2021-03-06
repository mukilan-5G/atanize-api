# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 12:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('phone_no', models.CharField(max_length=60)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='TypeOfWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
                ('base_salary', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TypeOfWork',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='type_of_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.TypeOfWork'),
        ),
    ]
