# Generated by Django 3.2.12 on 2023-03-24 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_course_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_topic',
            name='lesson',
            field=models.CharField(blank=True, max_length=100000),
        ),
    ]
