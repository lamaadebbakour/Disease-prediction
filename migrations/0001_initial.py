# Generated by Django 3.2.4 on 2021-08-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('DisId', models.AutoField(primary_key=True, serialize=False)),
                ('DisName', models.CharField(max_length=100)),
                ('DisDescribe', models.CharField(max_length=500)),
                ('specialty', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Docktur',
            fields=[
                ('DocId', models.AutoField(primary_key=True, serialize=False)),
                ('DocName', models.CharField(max_length=100)),
                ('Docspecialty', models.CharField(max_length=100)),
                ('docEmail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Sick',
            fields=[
                ('sickId', models.AutoField(primary_key=True, serialize=False)),
                ('sickName', models.CharField(max_length=100)),
                ('sickEmail', models.EmailField(max_length=254)),
            ],
        ),
    ]
