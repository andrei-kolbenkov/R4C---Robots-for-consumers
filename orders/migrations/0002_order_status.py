# Generated by Django 5.1.4 on 2024-12-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('waiting', 'Waiting'), ('completed', 'Completed')], default='waiting', max_length=20),
        ),
    ]
