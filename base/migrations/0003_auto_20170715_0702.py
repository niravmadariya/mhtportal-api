# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 07:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20170711_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='guardian_name',
        ),
        migrations.AddField(
            model_name='participant',
            name='father_mobile',
            field=models.CharField(default=0, help_text="Father's Mobile Number. Add +91 prefix", max_length=15, validators=[django.core.validators.RegexValidator(message="Mobile Number must be entered in the format:                    '+999999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='father_name',
            field=models.CharField(default='', help_text="Father's Name", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='mother_mobile',
            field=models.CharField(blank=True, help_text="Mother's Mobile Number. Add +91 prefix", max_length=15, validators=[django.core.validators.RegexValidator(message="Mobile Number must be entered in the format:                    '+999999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='participant',
            name='mother_name',
            field=models.CharField(blank=True, help_text="Mother's Name", max_length=50),
        ),
        migrations.AddField(
            model_name='participant',
            name='other_center',
            field=models.CharField(blank=True, help_text='First Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=6),
        ),
    ]