# Generated by Django 3.0.7 on 2020-07-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200705_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='Product',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='Username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carts',
            name='Username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(null=True, upload_to='uploadedprofileimages'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Phoneno',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='Username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='searched',
            name='Username',
            field=models.CharField(max_length=100),
        ),
    ]