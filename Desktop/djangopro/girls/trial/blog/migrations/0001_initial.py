# Generated by Django 2.2.10 on 2020-02-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passthing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=30)),
                ('device_key', models.CharField(max_length=20)),
                ('reg_date', models.DateTimeField(verbose_name='Registered Date')),
                ('dev_staus', models.IntegerField()),
            ],
        ),
    ]
