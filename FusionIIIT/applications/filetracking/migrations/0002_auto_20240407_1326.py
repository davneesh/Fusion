# Generated by Django 3.1.5 on 2024-04-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filetracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_extra_JSON',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='src_module',
            field=models.CharField(default='filetracking', max_length=100),
        ),
        migrations.AddField(
            model_name='file',
            name='src_object_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tracking',
            name='tracking_extra_JSON',
            field=models.JSONField(null=True),
        ),
    ]
