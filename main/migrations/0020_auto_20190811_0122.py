# Generated by Django 2.2.2 on 2019-08-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20190811_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='passing_year',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
