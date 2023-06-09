# Generated by Django 4.1.7 on 2023-04-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_delete_logos'),
    ]

    operations = [
        migrations.AddField(
            model_name='issued_items',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='issued_items',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]
