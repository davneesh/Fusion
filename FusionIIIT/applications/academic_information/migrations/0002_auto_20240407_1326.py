# Generated by Django 3.1.5 on 2024-04-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mother_name',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
