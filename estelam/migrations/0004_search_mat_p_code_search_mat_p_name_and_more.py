# Generated by Django 4.0.4 on 2023-07-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estelam', '0003_search_mat_file_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_mat',
            name='p_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='search_mat',
            name='p_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='search_mat',
            name='p_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
