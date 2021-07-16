# Generated by Django 3.1.4 on 2021-07-15 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0036_servicecategory_method_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('category', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date when created.', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date when updated.', null=True, verbose_name='Updated At')),
                ('title', models.CharField(blank=True, max_length=30)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('pages', models.IntegerField(blank=True, default=0)),
                ('published_date', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='books')),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customadmin.category')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
