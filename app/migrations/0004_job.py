# Generated by Django 3.2.12 on 2023-03-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=10000000)),
                ('address', models.CharField(blank=True, max_length=10000000)),
                ('country', models.CharField(blank=True, max_length=10000000)),
                ('website', models.CharField(blank=True, max_length=10000000)),
                ('role', models.CharField(blank=True, max_length=10000000)),
                ('work_experience', models.CharField(blank=True, max_length=10000000)),
                ('job_description', models.TextField(blank=True, max_length=10000000)),
                ('requirement', models.TextField(blank=True, max_length=10000000)),
            ],
        ),
    ]
