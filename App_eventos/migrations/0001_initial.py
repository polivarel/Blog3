# Generated by Django 4.1 on 2022-10-04 20:10

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(max_length=100, null=True)),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('subtitulo', models.CharField(max_length=100, null=True)),
                ('cuerpo', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('autor', models.CharField(max_length=100, null=True)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(default=None, upload_to='media/')),
            ],
        ),
    ]
