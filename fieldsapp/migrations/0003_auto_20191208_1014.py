# Generated by Django 2.1.5 on 2019-12-08 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fieldsapp', '0002_auto_20191208_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='locker_room',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='parking',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='shower',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 10, 14, 46, 664548, tzinfo=utc), verbose_name='date_pulished'),
        ),
    ]
