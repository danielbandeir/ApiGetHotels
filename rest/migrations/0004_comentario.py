# Generated by Django 2.2 on 2019-04-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_pessoa_senha'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomePessoa', models.CharField(max_length=255)),
                ('tempo', models.CharField(max_length=255)),
                ('foto', models.CharField(max_length=20000)),
                ('texto', models.CharField(max_length=255)),
            ],
        ),
    ]
