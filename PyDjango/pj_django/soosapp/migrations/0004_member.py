# Generated by Django 4.0.6 on 2022-07-29 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soosapp', '0003_gesipan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=50)),
                ('rdate', models.DateTimeField()),
                ('udate', models.DateTimeField()),
            ],
        ),
    ]
