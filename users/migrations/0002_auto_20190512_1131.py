# Generated by Django 2.2.1 on 2019-05-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthdat',
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateTimeField(null=True),
        ),
    ]