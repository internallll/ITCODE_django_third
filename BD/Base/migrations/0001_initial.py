# Generated by Django 5.1.1 on 2024-10-09 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusPark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone_number', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('logo', models.ImageField(upload_to='media')),
            ],
            options={
                'verbose_name': 'Автопарк',
                'verbose_name_plural': 'Автопарки',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, verbose_name='Госномер')),
                ('type_of_bus', models.CharField(max_length=255, verbose_name='Тип автобуса')),
                ('busPark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buses', to='Base.buspark', verbose_name='Автопарк')),
            ],
            options={
                'verbose_name': 'Автобус',
                'verbose_name_plural': 'Автобусы',
                'ordering': ['-number'],
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('job_title', models.CharField(max_length=255, verbose_name='Должность')),
                ('bus_park', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employers', to='Base.buspark', verbose_name='Автопарк')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
                'ordering': ['-surname'],
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_flight', models.DateField(verbose_name='Дата рейса')),
                ('time_of_flight', models.TimeField(verbose_name='Время рейса')),
                ('direction', models.CharField(max_length=255, verbose_name='Направление рейса')),
                ('employer', models.ManyToManyField(blank=True, null=True, related_name='flights', to='Base.employer', verbose_name='Рейсы')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название маршрута')),
                ('stay_1', models.CharField(max_length=255, verbose_name='Начальная остановка')),
                ('stay_2', models.CharField(max_length=255, verbose_name='Конечная остановка')),
                ('busPark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='Base.buspark', verbose_name='Автопарк')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ['-title'],
            },
        ),
    ]
