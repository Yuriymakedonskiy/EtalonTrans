# Generated by Django 3.2.16 on 2023-11-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtalonSite', '0019_auto_20231128_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf_cart',
            name='title',
            field=models.CharField(blank=True, max_length=80, unique=True),
        ),
    ]
