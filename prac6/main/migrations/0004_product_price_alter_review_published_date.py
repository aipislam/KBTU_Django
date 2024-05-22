# Generated by Django 5.0.1 on 2024-03-11 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_review_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=10000),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 17, 50, 30, 590926, tzinfo=datetime.timezone.utc)),
        ),
    ]