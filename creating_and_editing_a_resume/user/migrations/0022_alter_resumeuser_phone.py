# Generated by Django 4.2.7 on 2023-11-13 08:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_alter_education_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeuser',
            name='phone',
            field=models.CharField(blank=True, help_text='Укажите номер телефона для связи', validators=[django.core.validators.RegexValidator(message='Проверьте корректно ли указан номер телефона', regex='^(+?7|8)([\\d]{7,10})$')], verbose_name='Номер телефона'),
        ),
    ]