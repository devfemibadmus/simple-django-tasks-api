# Generated by Django 5.0.2 on 2024-09-20 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_rename_documents_document_rename_tasks_task_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='minWithdraw',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='user',
            name='rearns',
            field=models.FloatField(default=0.05),
        ),
    ]
