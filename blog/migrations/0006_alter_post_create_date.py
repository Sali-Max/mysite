# Generated by Django 5.0.3 on 2024-03-11 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_date_remove_post_email_post_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 11, 12, 2, 9, 233650, tzinfo=datetime.timezone.utc)),
        ),
    ]