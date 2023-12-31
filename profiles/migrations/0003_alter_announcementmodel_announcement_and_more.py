# Generated by Django 4.1.6 on 2023-09-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_massbookingmodel_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcementmodel',
            name='announcement',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='announcementmodel',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='announcementmodel',
            name='organization',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='massbookingmodel',
            name='intention',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='massbookingmodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='massbookingmodel',
            name='number',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='massbookingmodel',
            name='thanksgiving',
            field=models.BooleanField(),
        ),
    ]
