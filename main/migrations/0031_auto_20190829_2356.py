# Generated by Django 2.2.2 on 2019-08-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20190816_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='profile_picture',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
