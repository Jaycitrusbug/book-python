# Generated by Django 3.1.4 on 2021-07-16 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0038_auto_20210716_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created_at'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]