# Generated by Django 4.2.2 on 2024-01-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='designation',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=350),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
