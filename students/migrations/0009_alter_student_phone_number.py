# Generated by Django 3.2.4 on 2021-06-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_remove_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
