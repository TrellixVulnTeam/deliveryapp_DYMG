# Generated by Django 2.1.1 on 2018-11-20 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_Requests', '0006_auto_20181120_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stores',
            new_name='store',
        ),
    ]