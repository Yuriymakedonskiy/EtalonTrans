# Generated by Django 3.2.16 on 2023-11-22 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EtalonSite', '0009_massmedia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='massmedia',
            name='image',
        ),
    ]