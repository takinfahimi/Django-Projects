# Generated by Django 3.0.3 on 2020-04-04 10:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0029_auto_20200404_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_phonenumber',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,13}$')], verbose_name="User's mobile phone number"),
        ),
    ]