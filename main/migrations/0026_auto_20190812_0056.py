# Generated by Django 2.2.2 on 2019-08-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20190812_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='last_name',
        ),
    ]
