# Generated by Django 3.2.16 on 2023-10-31 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtalonSite', '0005_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
