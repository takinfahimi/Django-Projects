# Generated by Django 3.0.3 on 2020-03-26 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_auto_20200326_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='u_course',
            new_name='u_chosen_course',
        ),
    ]