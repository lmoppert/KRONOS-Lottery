# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dice', '0002_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='place',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='count',
            new_name='participant_number',
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
