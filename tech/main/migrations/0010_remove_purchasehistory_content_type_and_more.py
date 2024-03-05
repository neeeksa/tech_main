# Generated by Django 5.0.3 on 2024-03-05 10:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_purchasehistory_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasehistory',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='object_id',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='ingredient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.ingredient'),
        ),
        migrations.AlterField(
            model_name='purchasedingredient',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='purchase_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.DeleteModel(
            name='PurchasedMenuItem',
        ),
    ]
