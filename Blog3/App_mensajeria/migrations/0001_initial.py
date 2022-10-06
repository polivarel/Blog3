# Generated by Django 4.1 on 2022-10-05 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mensajes_db',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('emisor', models.CharField(max_length=100)),
                ('receptor', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
