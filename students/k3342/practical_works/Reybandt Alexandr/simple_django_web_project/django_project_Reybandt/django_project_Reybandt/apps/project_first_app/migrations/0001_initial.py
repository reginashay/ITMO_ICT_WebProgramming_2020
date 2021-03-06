# Generated by Django 3.0.4 on 2020-03-21 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_id', models.IntegerField(verbose_name='Номер удостоверения')),
                ('date_of_issue', models.DateField(verbose_name='Дата выдачи')),
                ('license_type', models.CharField(choices=[('A', 'Мотоциклы'), ('B', 'Легковые авто'), ('C', 'Грузовики'), ('D', 'Автобусы'), ('M', 'Мопеды')], max_length=1)),
                ('car_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.CarOwner')),
            ],
        ),
    ]
