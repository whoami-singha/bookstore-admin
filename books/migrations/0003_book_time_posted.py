# Generated by Django 4.1.5 on 2023-02-19 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='time_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
