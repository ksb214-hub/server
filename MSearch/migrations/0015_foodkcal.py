# Generated by Django 5.0.4 on 2024-05-12 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSearch', '0014_crawleddata_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodKcal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('servingsize', models.CharField(max_length=300)),
                ('kcal', models.CharField(max_length=300)),
                ('carbohydrate', models.CharField(max_length=300)),
                ('protein', models.CharField(max_length=300)),
                ('fat', models.CharField(max_length=300)),
                ('sugars', models.CharField(max_length=300)),
                ('salt', models.CharField(max_length=300)),
                ('cholesterol', models.CharField(max_length=300)),
                ('saturatedfat', models.CharField(max_length=300)),
                ('transfat', models.CharField(max_length=300)),
            ],
        ),
    ]