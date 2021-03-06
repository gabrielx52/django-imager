# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=180, null=True)),
                ('website', models.URLField()),
                ('fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('phone', models.CharField(max_length=12)),
                ('bio', models.TextField(max_length=500)),
                ('camera', models.CharField(choices=[('FL', 'Film'), ('DG', 'Digital'), ('PL', 'Polaroid'), ('DG', 'Daguerreotype')], max_length=2)),
                ('photo_style', models.CharField(choices=[('PR', 'Portrait'), ('SL', 'Still Life'), ('NT', 'Nature'), ('AB', 'Abstract'), ('FS', 'Fashion'), ('AD', 'Advertising'), ('WL', 'Wildlife'), ('WD', 'Wedding'), ('BW', 'Black and White'), ('MC', 'Macro'), ('TP', 'Time Lapse'), ('LS', 'Landscape'), ('SP', 'Sports')], max_length=2)),
                ('service', models.CharField(choices=[('SS', 'Session'), ('ED', 'Editing'), ('CL', 'Coloring'), ('PT', 'Printing'), ('FR', 'Framing'), ('AV', 'Advertising'), ('TV', 'Travel')], max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
