# Generated by Django 4.1.7 on 2023-09-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_profile_id_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(default=1),
        ),
    ]