# Generated by Django 5.0.1 on 2024-02-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_account_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
