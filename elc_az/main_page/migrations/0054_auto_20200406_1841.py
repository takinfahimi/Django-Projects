# Generated by Django 3.0.3 on 2020-04-06 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0053_auto_20200406_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_phonenumber',
            field=models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\d{7}$')]),
        ),
    ]
