# Generated by Django 4.1.7 on 2023-09-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live_Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('date_send', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
