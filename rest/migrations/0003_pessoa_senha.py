# Generated by Django 2.2 on 2019-04-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='senha',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]