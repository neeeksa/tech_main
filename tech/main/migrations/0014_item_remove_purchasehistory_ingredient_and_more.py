# Generated by Django 5.0.3 on 2024-03-05 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_purchasemenuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.item'),
        ),
    ]
