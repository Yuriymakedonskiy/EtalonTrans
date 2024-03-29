# Generated by Django 3.2.16 on 2023-12-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtalonSite', '0021_alter_pdf_cart_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='Telegram',
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, unique=True, upload_to='docx/'),
        ),
        migrations.AlterField(
            model_name='massmedia',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='docx/'),
        ),
        migrations.AlterField(
            model_name='pdf_cart',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/docx/'),
        ),
    ]
