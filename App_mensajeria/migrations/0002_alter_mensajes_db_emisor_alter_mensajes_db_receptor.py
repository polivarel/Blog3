# Generated by Django 4.1 on 2022-10-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_mensajeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes_db',
            name='emisor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mensajes_db',
            name='receptor',
            field=models.IntegerField(),
        ),
    ]
