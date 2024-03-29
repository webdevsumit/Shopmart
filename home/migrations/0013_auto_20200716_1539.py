# Generated by Django 3.0.7 on 2020-07-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200715_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Oredered',
            new_name='Ordered',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='Price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='OfferPrice',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.FloatField(),
        ),
    ]
