# Generated by Django 2.2 on 2022-07-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
    ]
