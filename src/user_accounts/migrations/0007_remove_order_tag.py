# Generated by Django 3.2.2 on 2021-05-07 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0006_auto_20210507_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
    ]
