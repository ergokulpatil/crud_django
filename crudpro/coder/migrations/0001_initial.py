# Generated by Django 3.2.12 on 2023-09-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='codermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=44)),
                ('designation', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
