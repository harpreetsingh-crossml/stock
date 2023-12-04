# Generated by Django 4.2.6 on 2023-11-30 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userside', '0004_rename_purchase_price_stocktransaction_price_per_share_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockBuy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=10)),
                ('shares', models.PositiveIntegerField()),
                ('purchase_price', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('shares', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=10000.0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='StockTransaction',
        ),
    ]
