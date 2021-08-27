# Generated by Django 3.2.6 on 2021-08-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20210818_0136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockprice',
            name='diff',
        ),
        migrations.AddField(
            model_name='stockprice',
            name='fluc_rate',
            field=models.CharField(default='0.0', max_length=15),
        ),
        migrations.AddField(
            model_name='stockprice',
            name='low',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stockprice',
            name='trad_value',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='close',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='high',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='open',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockprice',
            name='volume',
            field=models.IntegerField(default=0),
        ),
    ]
