# Generated by Django 5.0.7 on 2024-08-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=0, verbose_name='Количество на складе'),
        ),
    ]
