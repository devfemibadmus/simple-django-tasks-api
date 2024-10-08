# Generated by Django 5.0.2 on 2024-09-10 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_tasks_description_alter_tasks_title_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='title',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='history',
            name='action',
            field=models.CharField(choices=[('debit', 'debit'), ('credit', 'credit'), ('pending debit', 'pending debit'), ('pending credit', 'pending credit')], max_length=15),
        ),
    ]
