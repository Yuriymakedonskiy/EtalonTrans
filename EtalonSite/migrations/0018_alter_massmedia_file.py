# Generated by Django 3.2.16 on 2023-11-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtalonSite', '0017_auto_20231124_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='massmedia',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
    ]