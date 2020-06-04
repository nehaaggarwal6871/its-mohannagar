# Generated by Django 2.2.2 on 2019-09-08 09:58

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone
import main.json


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_events_upcomming'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='raghav', max_length=200, null=True)),
                ('email', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, default=main.json.email, null=True, size=None)),
                ('time', models.TimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
