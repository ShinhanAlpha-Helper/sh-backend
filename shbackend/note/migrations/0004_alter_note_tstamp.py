# Generated by Django 4.1.6 on 2023-02-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_alter_note_tstamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tstamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록일시'),
        ),
    ]
