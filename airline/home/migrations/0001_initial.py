# Generated by Django 4.0.5 on 2022-07-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availableAmount', models.IntegerField()),
                ('detail', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('displayPrice', models.CharField(max_length=200)),
            ],
        ),
    ]
