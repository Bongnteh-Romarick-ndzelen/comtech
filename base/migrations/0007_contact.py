# Generated by Django 4.1.7 on 2023-09-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_profile_id_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('subject', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
