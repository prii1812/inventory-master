# Generated by Django 4.1.7 on 2023-04-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_rename_is_accepted_issued_items_accepted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issued_items',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='issued_items',
            name='rejected',
        ),
        migrations.AddField(
            model_name='issued_items',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]