# Generated by Django 4.0.6 on 2022-07-27 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soosapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='rdate',
            field=models.DateTimeField(),
        ),
    ]
