# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0007_recurso_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='referencia',
            field=models.CharField(default=b'b0f29fe1', editable=False, max_length=8),
        ),
    ]
