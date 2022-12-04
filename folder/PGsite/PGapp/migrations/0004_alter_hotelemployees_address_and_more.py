# Generated by Django 4.1.3 on 2022-11-20 11:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PGapp', '0003_hotelemployees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelemployees',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Employee address'),
        ),
        migrations.AlterField(
            model_name='hotelemployees',
            name='birth_date',
            field=models.DateField(verbose_name='Employee birth date'),
        ),
        migrations.AlterField(
            model_name='hotelemployees',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Employee first name'),
        ),
        migrations.AlterField(
            model_name='hotelemployees',
            name='hire_date',
            field=models.DateField(auto_now=True, verbose_name='Employee hire date'),
        ),
        migrations.AlterField(
            model_name='hotelemployees',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Employee last name'),
        ),
        migrations.AlterField(
            model_name='hotelemployees',
            name='phone',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Employee phone'),
        ),
        migrations.AlterField(
            model_name='hotelemployees',
            name='photo',
            field=models.ImageField(blank=True, height_field=140, null=True, upload_to='', verbose_name='Employee photo', width_field=140),
        ),
    ]