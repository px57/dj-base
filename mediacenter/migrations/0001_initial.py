# Generated by Django 4.2 on 2023-10-24 22:31

from django.db import migrations, models
import django.db.models.deletion
import mediacenter.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('file_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('src', models.FileField(blank=True, default=None, null=True, upload_to=mediacenter.models.dynamic_upload_to)),
                ('md5', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('label', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('disk_size', models.IntegerField(blank=True, default=None, null=True)),
                ('autocropped_size', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('mime_type', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('resolutions', models.JSONField(blank=True, default={'height': None, 'width': None}, null=True)),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FilesPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('file', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mediacenter.filesmodel')),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
    ]