# Generated by Django 5.0.2 on 2024-09-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_alter_user_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_time',
            field=models.JSONField(default=list),
        ),
    ]
