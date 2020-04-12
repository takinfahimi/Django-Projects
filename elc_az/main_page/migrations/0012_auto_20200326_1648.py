# Generated by Django 3.0.3 on 2020-03-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0011_auto_20200321_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_chosen_course',
            field=models.CharField(choices=[('eng1', 'English Level 1'), ('ru1', 'Rus dili 1'), ('fr1', 'Fransız Dili')], default='No course chosen', max_length=30, verbose_name='The course the user registered for'),
        ),
    ]
