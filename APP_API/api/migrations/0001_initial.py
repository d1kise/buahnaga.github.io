# Generated by Django 4.1.5 on 2023-01-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ebrand', models.CharField(max_length=100)),
                ('emodel', models.CharField(max_length=100)),
                ('eprice', models.IntegerField()),
            ],
        ),
    ]
