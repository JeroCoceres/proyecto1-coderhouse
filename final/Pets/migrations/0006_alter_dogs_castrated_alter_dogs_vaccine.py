# Generated by Django 4.1.5 on 2023-01-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pets', '0005_alter_dogs_castrated_alter_dogs_vaccine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs',
            name='castrated',
            field=models.BooleanField(verbose_name='Castrado'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='vaccine',
            field=models.BooleanField(verbose_name='Vacunado'),
        ),
    ]
