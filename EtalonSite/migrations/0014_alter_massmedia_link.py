# Generated by Django 3.2.16 on 2023-11-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtalonSite', '0013_auto_20231122_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massmedia',
            name='link',
            field=models.TextField(),
        ),
    ]