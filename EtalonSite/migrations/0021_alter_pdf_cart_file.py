# Generated by Django 3.2.16 on 2023-11-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtalonSite', '0020_pdf_cart_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf_cart',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/docs/'),
        ),
    ]