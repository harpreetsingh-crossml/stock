# Generated by Django 4.2.6 on 2023-11-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
