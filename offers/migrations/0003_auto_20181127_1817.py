# Generated by Django 2.1.2 on 2018-11-27 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belongings', '0003_belonging_img'),
        ('offers', '0002_auto_20181105_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='BelongingsPerOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belonging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belongings.Belonging')),
            ],
        ),
        migrations.RemoveField(
            model_name='offer',
            name='offered_object',
        ),
        migrations.AddField(
            model_name='belongingsperoffer',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.Offer'),
        ),
    ]
