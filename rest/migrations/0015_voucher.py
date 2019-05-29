# Generated by Django 2.1.7 on 2019-05-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0014_auto_20190509_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageUrl', models.CharField(max_length=3000)),
                ('nameVoucher', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('partner', models.CharField(max_length=255)),
                ('typeVoucher', models.CharField(max_length=255)),
                ('instructions', models.CharField(max_length=255)),
                ('minBuy', models.CharField(max_length=255)),
                ('maxBuy', models.CharField(max_length=255)),
                ('cMin', models.CharField(max_length=255)),
                ('valitityDe', models.CharField(max_length=255)),
                ('valitityAte', models.CharField(max_length=255)),
                ('rescue', models.CharField(max_length=255)),
                ('useOnly', models.CharField(max_length=255)),
            ],
        ),
    ]