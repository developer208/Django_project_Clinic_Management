# Generated by Django 4.0.2 on 2022-04-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_patientdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='patientClone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
            ],
        ),
    ]
