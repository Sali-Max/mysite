# Generated by Django 5.0.3 on 2024-03-11 11:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_delete_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
