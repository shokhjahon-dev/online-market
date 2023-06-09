# Generated by Django 4.2.1 on 2023-05-06 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kategoriya nomi')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='Kategoriyasi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mahsulot nomi')),
                ('full_name', models.CharField(max_length=100, verbose_name="Mahsulotning to'liq nomi")),
                ('description', models.TextField(verbose_name="Mahsulot haqida ma'lumot")),
                ('product_img', models.ImageField(upload_to='product_images', verbose_name='Mahsulot rasmi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Mahsulot narxi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Kategoriyasi')),
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
    ]
