# Generated by Django 2.2 on 2019-06-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190611_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='max_connected_devices',
            field=models.IntegerField(default=2, verbose_name='max_connected_devices'),
        ),
        migrations.AddField(
            model_name='profile',
            name='connected_devices',
            field=models.IntegerField(default=0, verbose_name='connected_devices'),
        ),
    ]
