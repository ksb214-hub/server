# Generated by Django 5.0.4 on 2024-04-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSearch', '0007_alter_myfoodbankmodel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRecipy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('clss', models.CharField(max_length=100, verbose_name='clss')),
                ('ingt', models.CharField(max_length=100, verbose_name='ingt')),
                ('foodnm', models.CharField(max_length=100, verbose_name='foodnm')),
                ('fooddscrt', models.CharField(max_length=100, verbose_name='fooddscrt')),
                ('foodmntr', models.CharField(max_length=100, verbose_name='clss')),
                ('cookmth', models.CharField(max_length=100, verbose_name='foodnm')),
                ('cookdsrt', models.CharField(max_length=100, verbose_name='fooddscrt')),
                ('url', models.CharField(max_length=100, verbose_name='clss')),
            ],
        ),
    ]