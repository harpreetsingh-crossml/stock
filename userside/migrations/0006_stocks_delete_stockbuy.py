# Generated by Django 4.2.6 on 2023-12-04 05:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userside', '0005_stockbuy_stocksell_alter_userprofile_balance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('shares', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('total', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000)])),
                ('purchase_price', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='StockBuy',
        ),
    ]