# Generated by Django 5.0.4 on 2024-04-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSearch', '0006_foodcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfoodbankmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]