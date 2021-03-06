# Generated by Django 3.2.6 on 2021-08-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='code',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='code_isin',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='homepage',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='industry',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='listing_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='market',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='representative',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sector',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='settle_month',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
