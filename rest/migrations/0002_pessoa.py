# Generated by Django 2.2 on 2019-04-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=15)),
                ('foto', models.CharField(max_length=20000)),
            ],
        ),
    ]