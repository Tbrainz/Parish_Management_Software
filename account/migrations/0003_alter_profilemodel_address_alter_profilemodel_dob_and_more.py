# Generated by Django 4.1.6 on 2023-09-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profilemodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='dob',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='full_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('single', 'single'), ('married', 'married'), ('widow', 'widow'), ('widower', 'widower')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='number',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='societies',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='tribe',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
