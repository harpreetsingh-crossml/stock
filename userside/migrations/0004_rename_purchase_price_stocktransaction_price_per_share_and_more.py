# Generated by Django 4.2.6 on 2023-11-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0003_holding_portfolio_remove_stock_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocktransaction',
            old_name='purchase_price',
            new_name='price_per_share',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='purchase_date',
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='cash_balance',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Holding',
        ),
    ]
