# Generated by Django 5.1.2 on 2024-12-17 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_room_options_room_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
