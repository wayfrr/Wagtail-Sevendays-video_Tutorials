# Generated by Django 3.2.6 on 2021-08-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='Welcome to my home Home Page', max_length=100),
        ),
    ]
