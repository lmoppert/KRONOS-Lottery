# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dice', '0003_auto_20150202_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='diced',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
