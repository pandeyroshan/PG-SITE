# Generated by Django 2.1.5 on 2019-06-23 21:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='shortNote',
            field=models.TextField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]