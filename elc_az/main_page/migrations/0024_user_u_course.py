# Generated by Django 3.0.3 on 2020-04-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0023_remove_user_u_chosen_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='u_course',
            field=models.CharField(choices=[('EN', 'English Level 1'), ('RU', 'Rus dili 1'), ('FR', 'Fransız Dili')], default='RU', max_length=2),
        ),
    ]