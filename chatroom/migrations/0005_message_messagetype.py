# Generated by Django 4.2 on 2023-11-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0004_message_joinedfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='messageType',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]