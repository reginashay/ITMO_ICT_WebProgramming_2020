# Generated by Django 2.0.6 on 2020-05-20 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.IntegerField(max_length=1)),
                ('grade', models.IntegerField(choices=[(2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('name', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('non-binary', 'non-binary')], max_length=10)),
                ('study_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('floor', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sub_type', models.CharField(choices=[('major', 'major'), ('minor', 'minor')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('non-binary', 'non-binary')], max_length=10)),
                ('experience', models.CharField(max_length=50)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], max_length=3)),
                ('lesson_num', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], max_length=1)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Room')),
                ('study_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(through='school.Teaching', to='school.Subject'),
        ),
        migrations.AddField(
            model_name='room',
            name='subject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Subject'),
        ),
        migrations.AddField(
            model_name='class',
            name='guiding_teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='pupil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Pupil'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Subject'),
        ),
    ]