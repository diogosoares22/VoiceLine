# Generated by Django 3.2.5 on 2022-02-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='language',
        ),
        migrations.AddField(
            model_name='record',
            name='text',
            field=models.CharField(default='Default Text', max_length=200),
        ),
    ]
