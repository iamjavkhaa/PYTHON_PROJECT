# Generated by Django 4.0.5 on 2022-07-02 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_carttest'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartTestTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='carttest',
            name='pro_id',
        ),
    ]
