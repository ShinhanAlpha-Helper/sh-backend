# Generated by Django 4.1.6 on 2023-02-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_alter_note_tstamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]