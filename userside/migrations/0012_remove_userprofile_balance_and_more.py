# Generated by Django 4.2.6 on 2023-12-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0011_transaction_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='balance',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='account_balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]