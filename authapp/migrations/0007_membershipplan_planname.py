# Generated by Django 4.1 on 2022-09-16 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_attendance_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipplan',
            name='planName',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
