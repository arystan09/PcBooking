# Generated by Django 5.1.2 on 2024-10-31 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_club_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='postal_code',
            field=models.CharField(max_length=10, null=True, verbose_name='Почтовый Индекс'),
        ),
    ]
