# Generated by Django 3.2.11 on 2022-01-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('week4', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
