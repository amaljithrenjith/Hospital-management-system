# Generated by Django 4.1.2 on 2022-11-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_name', models.CharField(max_length=225)),
                ('dot_name', models.CharField(max_length=225)),
                ('dept_name', models.CharField(max_length=225)),
                ('ph_no', models.IntegerField()),
                ('symptmas', models.CharField(max_length=350)),
                ('date', models.DateField()),
            ],
        ),
    ]
