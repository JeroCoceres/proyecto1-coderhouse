# Generated by Django 4.1.5 on 2023-01-09 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pets', '0003_alter_cats_options_alter_dogs_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cats',
            name='adoption_date',
        ),
        migrations.RemoveField(
            model_name='cats',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='dogs',
            name='adoption_date',
        ),
        migrations.RemoveField(
            model_name='dogs',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='more_pets',
            name='adoption_date',
        ),
        migrations.RemoveField(
            model_name='more_pets',
            name='birth',
        ),
    ]
