# Generated by Django 4.1 on 2022-10-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento_db',
            name='imagen',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
