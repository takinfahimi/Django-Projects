# Generated by Django 3.0.3 on 2020-04-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0040_auto_20200405_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_phoneprefix',
            field=models.CharField(choices=[('', ''), ('AZE1', '050'), ('AZE2', '051'), ('BAK1', '055'), ('BAK2', '099'), ('NAR1', '070'), ('NAR2', '077')], max_length=5, verbose_name='Phone prefix '),
        ),
    ]
