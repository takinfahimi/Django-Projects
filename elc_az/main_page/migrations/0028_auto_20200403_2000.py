# Generated by Django 3.0.3 on 2020-04-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0027_auto_20200403_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_course',
            field=models.CharField(choices=[('', ''), ('Rus', 'Rus dili 1'), ('Fra', 'Fransız Dili'), ('Eng', 'English Level 1'), ('Alm', 'Alman dili')], default='Rus', max_length=20, verbose_name="User's course(s)"),
        ),
    ]
