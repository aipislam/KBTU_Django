# Generated by Django 5.0.4 on 2024-05-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_text',
            field=models.TextField(default='Your product status updated!', max_length=255),
        ),
    ]
