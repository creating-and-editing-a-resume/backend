# Generated by Django 4.2.7 on 2023-11-12 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_education_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 11, 12, 19, 39, 2, 124952, tzinfo=datetime.timezone.utc), help_text='Дата окончания', null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 11, 12, 19, 39, 2, 126983, tzinfo=datetime.timezone.utc), help_text='Дата окончания работы', null=True, verbose_name='Дата окончания работы'),
        ),
    ]
