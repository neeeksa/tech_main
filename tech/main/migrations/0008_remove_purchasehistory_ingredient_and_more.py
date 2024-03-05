# Generated by Django 5.0.3 on 2024-03-05 10:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0007_purchasedmenuitem_delete_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasehistory',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='purchasedmenuitem',
            name='purchase',
            field=models.ForeignKey(default=0.0, on_delete=django.db.models.deletion.CASCADE, to='main.purchase'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='purchase_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
