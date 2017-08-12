# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-12 12:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0003_gameinstance_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='gameinstance',
            name='Players',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gameinstance',
            name='State',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='spot',
            name='Deck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.Deck'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='GameInstance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.GameInstance'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='Target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='Tags',
            field=models.ManyToManyField(to='cards.Tag'),
        ),
    ]
