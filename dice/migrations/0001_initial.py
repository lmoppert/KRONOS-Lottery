# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schedule', models.DateField()),
                ('place', models.CharField(max_length=200, blank=True)),
                ('description', models.TextField(blank=True)),
                ('count', models.IntegerField()),
                ('deadline', models.DateField()),
                ('candidates', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='dice.Candidate')),
                ('responsible', models.ForeignKey(related_name='event_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='candidate',
            name='event',
            field=models.ForeignKey(to='dice.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
