# Generated by Django 2.0.6 on 2020-05-29 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20200528_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='study_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.Class'),
        ),
    ]