# Generated by Django 5.0.2 on 2024-09-24 03:07

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_user_last_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_time',
            field=models.JSONField(default=api.models.User.last_time_default),
        ),
    ]
