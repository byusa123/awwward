# Generated by Django 3.1.2 on 2020-10-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0002_location_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact',
            field=models.IntegerField(default=0),
        ),
    ]
