# Generated by Django 4.2.4 on 2023-09-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_course_seat_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='seat_available',
            field=models.IntegerField(default=0),
        ),
    ]
