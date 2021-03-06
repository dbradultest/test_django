# Generated by Django 3.2.4 on 2021-06-13 11:23

import datetime
import django.core.validators
from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20210613_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='graduate_date2',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(
                default=datetime.date.today,
                validators=[students.validators.adult_validator],
            ),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(
                max_length=80, validators=[django.core.validators.MinLengthValidator(2)]
            ),
        ),
    ]
