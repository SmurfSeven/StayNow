# Generated by Django 3.2.4 on 2021-06-20 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('ciudad', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField()),
                ('camas', models.IntegerField()),
            ],
        ),
    ]
