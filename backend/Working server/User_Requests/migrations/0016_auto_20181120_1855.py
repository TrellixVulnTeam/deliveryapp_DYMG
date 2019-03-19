# Generated by Django 2.1.1 on 2018-11-20 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Requests', '0015_auto_20181120_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderQuantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderedProduct',
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity1',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity10',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity2',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity3',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity4',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity5',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity6',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity7',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity8',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderQuantity9',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct10',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct2',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct3',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct4',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct5',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct6',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct7',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct8',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct9',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]