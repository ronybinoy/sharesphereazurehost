# Generated by Django 4.2.4 on 2023-09-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_seat_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='rejection_remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]