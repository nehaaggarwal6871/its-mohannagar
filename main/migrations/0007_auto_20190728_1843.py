# Generated by Django 2.2.2 on 2019-07-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190728_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='contact',
            field=models.CharField(blank=True, default={'address': '', 'email': '', 'phone': ''}, max_length=10000),
        ),
        # migrations.AlterField(
        #     model_name='teammember',
        #     name='education',
        #     field=models.CharField(blank=True, default={'education': ['Education1', 'Education2']}, max_length=10000),
        # ),
        migrations.AlterField(
            model_name='teammember',
            name='links',
            field=models.CharField(blank=True, default={'facebook': 'https://www.facebook.com/', 'github': 'https://github.com/', 'twitter': 'https://twitter.com'}, max_length=10000),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='skills',
            field=models.CharField(blank=True, default={'skill': ['skill1', 'skill2']}, max_length=10000),
        ),
    ]
