# Generated by Django 4.1.5 on 2023-01-08 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vaccine', models.BooleanField()),
                ('birth', models.DateField()),
                ('adoption_date', models.DateField()),
                ('castrated', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vaccine', models.BooleanField()),
                ('birth', models.DateField()),
                ('adoption_date', models.DateField()),
                ('castrated', models.BooleanField()),
            ],
        ),
    ]
