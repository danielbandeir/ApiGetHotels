# Generated by Django 2.1.7 on 2019-04-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0010_isdebug'),
    ]

    operations = [
        migrations.CreateModel(
            name='skin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagemSpash', models.CharField(max_length=3000)),
                ('imagemCapa', models.CharField(max_length=3000)),
                ('cor1', models.CharField(max_length=22)),
                ('cor2', models.CharField(max_length=22)),
                ('cor3', models.CharField(max_length=22)),
                ('cor4', models.CharField(max_length=22)),
                ('cor5', models.CharField(max_length=22)),
                ('cor6', models.CharField(max_length=22)),
                ('cor7', models.CharField(max_length=22)),
                ('cor8', models.CharField(max_length=22)),
                ('cor9', models.CharField(max_length=22)),
                ('cor10', models.CharField(max_length=22)),
            ],
        ),
    ]
