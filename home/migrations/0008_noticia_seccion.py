# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-22 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180222_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='seccion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Categoria'),
            preserve_default=False,
        ),
    ]
