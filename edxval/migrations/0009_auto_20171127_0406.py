# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edxval', '0008_remove_subtitles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcriptpreference',
            name='three_play_turnaround',
            field=models.CharField(blank=True, choices=[(b'extended', b'10-Day/Extended'), (b'standard', b'4-Day/Standard'), (b'expedited', b'2-Day/Expedited'), (b'rush', b'24 hour/Rush'), (b'same_day', b'Same Day'), (b'two_hour', b'2 Hour')], max_length=20, null=True, verbose_name=b'3PlayMedia Turnaround'),
        ),
    ]
