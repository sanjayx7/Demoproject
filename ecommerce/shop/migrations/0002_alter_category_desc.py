# Generated by Django 5.0.1 on 2024-01-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.TextField(default=0),
        ),
    ]