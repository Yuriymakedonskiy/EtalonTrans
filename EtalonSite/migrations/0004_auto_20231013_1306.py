# Generated by Django 3.2.16 on 2023-10-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EtalonSite', '0003_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTelegram', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='idTelegram',
        ),
    ]
