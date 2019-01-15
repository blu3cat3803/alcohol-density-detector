# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-24 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0003_auto_20181223_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='alcohol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t', models.DecimalField(decimal_places=0, max_digits=9)),
                ('v1', models.DecimalField(decimal_places=1, max_digits=5)),
                ('v2', models.DecimalField(decimal_places=1, max_digits=5)),
                ('v3', models.DecimalField(decimal_places=1, max_digits=5)),
                ('v4', models.DecimalField(decimal_places=1, max_digits=5)),
                ('v5', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='alcohol_1',
        ),
    ]
