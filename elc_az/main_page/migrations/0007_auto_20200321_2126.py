# Generated by Django 3.0.2 on 2020-03-21 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_user_u_chosen_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_chosen_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_page.course'),
        ),
    ]