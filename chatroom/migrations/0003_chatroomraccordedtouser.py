# Generated by Django 4.2 on 2023-10-01 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('chatroom', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoomRaccordedToUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('chatroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatroom_raccorded_to_user', to='chatroom.chatroom')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatroom_raccorded_to_user', to='profiles.profile')),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
    ]
