# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-23 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_noticia_seccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now=True)),
                ('correo', models.CharField(max_length=30)),
                ('datos', models.CharField(max_length=100)),
            ],
        ),
    ]
