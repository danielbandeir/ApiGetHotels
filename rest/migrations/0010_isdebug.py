# Generated by Django 2.1.7 on 2019-04-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0009_linkservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='isDebug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=1024)),
            ],
        ),
    ]
