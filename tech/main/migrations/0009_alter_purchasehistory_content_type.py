# Generated by Django 5.0.3 on 2024-03-05 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0008_remove_purchasehistory_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasehistory',
            name='content_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
