# Generated by Django 2.1.7 on 2019-04-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0008_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='linkService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=1024)),
            ],
        ),
    ]
