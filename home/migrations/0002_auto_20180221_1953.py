# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-21 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Noticia',
            new_name='Noticias',
        ),
    ]