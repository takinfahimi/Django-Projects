# Generated by Django 3.0.3 on 2020-03-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0016_auto_20200326_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_chosen_course',
            field=models.CharField(default='No course chosen', max_length=30, verbose_name='The course the user registered for'),
        ),
    ]