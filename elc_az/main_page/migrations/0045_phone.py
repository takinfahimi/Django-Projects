# Generated by Django 3.0.3 on 2020-04-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0044_auto_20200405_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('prefix_id', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Prefix_ID')),
                ('prefix_string', models.CharField(max_length=3, verbose_name='Prefix_string')),
                ('prefix_description', models.TextField()),
            ],
        ),
    ]
