# Generated by Django 5.0.1 on 2024-03-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='university',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]