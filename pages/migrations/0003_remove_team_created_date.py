# Generated by Django 3.0.12 on 2021-02-03 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_team_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='created_date',
        ),
    ]
