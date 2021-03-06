# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_auto_20161108_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='data_final',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='data_inicial',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='recurso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos.Recurso'),
        ),
        migrations.AddField(
            model_name='agendamento',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recursos.Funcionario'),
        ),
    ]
