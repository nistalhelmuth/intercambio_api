# Generated by Django 2.1.2 on 2018-11-04 23:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0002_auto_20181024_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
