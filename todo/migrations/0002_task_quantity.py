# Generated by Django 3.0.9 on 2020-11-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
