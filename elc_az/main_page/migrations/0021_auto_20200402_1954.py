# Generated by Django 3.0.3 on 2020-04-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0020_auto_20200402_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_chosen_course',
            field=models.CharField(blank=True, choices=[('EN', 'English Level 1'), ('RU', 'Rus dili 1'), ('FR', 'Fransız Dili')], default='RU', max_length=20),
        ),
    ]