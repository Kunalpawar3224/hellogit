# Generated by Django 4.1.5 on 2023-02-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=30)),
                ('contant_number', models.IntegerField(max_length=10)),
                ('emial_id', models.TextField()),
            ],
        ),
    ]