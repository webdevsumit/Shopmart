# Generated by Django 3.0.7 on 2020-07-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200711_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='Catagory',
            field=models.CharField(max_length=70),
        ),
    ]