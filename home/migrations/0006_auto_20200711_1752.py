# Generated by Django 3.0.7 on 2020-07-11 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200710_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Catagory',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.catagory'),
        ),
    ]
