# Generated by Django 5.0 on 2023-12-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event_Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
