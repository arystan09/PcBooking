# Generated by Django 5.1.2 on 2024-10-31 04:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_club_district_club_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='instagram_url',
            field=models.URLField(default=1, verbose_name='Instagram'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=9, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=9, verbose_name='Долгота'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='twogis_url',
            field=models.URLField(default=1, verbose_name='2gis'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='website',
            field=models.URLField(default=1, verbose_name='Сайт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='club',
            name='whatsapp_url',
            field=models.URLField(default=1, verbose_name='Whatsapp'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='club',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='club',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='club',
            name='district',
            field=models.CharField(max_length=100, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название Клуба'),
        ),
        migrations.AlterField(
            model_name='club',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name='Почтовый Индекс'),
        ),
        migrations.AlterField(
            model_name='club',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='club',
            name='work_time_end',
            field=models.TimeField(verbose_name='Время Закрытия'),
        ),
        migrations.AlterField(
            model_name='club',
            name='work_time_start',
            field=models.TimeField(verbose_name='Время Открытия'),
        ),
        migrations.AlterField(
            model_name='club',
            name='x_size',
            field=models.IntegerField(verbose_name='Размер по X'),
        ),
        migrations.AlterField(
            model_name='club',
            name='y_size',
            field=models.IntegerField(verbose_name='Размер по Y'),
        ),
    ]
