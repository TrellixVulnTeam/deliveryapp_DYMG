# Generated by Django 2.1.1 on 2018-11-20 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Requests', '0014_auto_20181120_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderedProduct',
        ),
        migrations.AddField(
            model_name='order',
            name='orderedProduct',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
