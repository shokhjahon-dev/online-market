# Generated by Django 4.2.1 on 2023-05-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='income_id',
            field=models.CharField(default='#0080b5e0-42b6-48a6-b02e-7a77c8e650c5', max_length=255, verbose_name='Mahsulot ID raqami'),
        ),
    ]
