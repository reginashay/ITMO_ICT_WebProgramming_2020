# Generated by Django 3.0.6 on 2020-05-27 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airport_app', '0002_flight_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrivaldeparture',
            name='plane',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='airport_app.Plane'),
            preserve_default=False,
        ),
    ]
