# Generated by Django 3.0.2 on 2020-03-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20200304_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_shx_pin',
            field=models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='user IDcard pin'),
        ),
    ]
