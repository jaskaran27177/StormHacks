# Generated by Django 3.1.7 on 2021-02-21 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20210221_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]