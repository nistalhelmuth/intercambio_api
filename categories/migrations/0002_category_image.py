# Generated by Django 2.1.2 on 2018-11-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.URLField(default='https://pre00.deviantart.net/5327/th/pre/f/2016/190/e/7/e70644a78303cfd323f333bc229d82d0-da8s1s1.png', max_length=500),
            preserve_default=False,
        ),
    ]