# Generated by Django 2.2.4 on 2019-08-17 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190817_1410'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reader',
            new_name='User',
        ),
    ]
