# Generated by Django 2.0 on 2019-02-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='贝里余额'),
        ),
    ]
