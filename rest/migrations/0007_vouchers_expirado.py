# Generated by Django 2.2 on 2019-04-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_vouchers'),
    ]

    operations = [
        migrations.AddField(
            model_name='vouchers',
            name='expirado',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
