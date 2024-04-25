# Generated by Django 4.2.7 on 2024-04-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.RemoveField(
            model_name='products',
            name='content',
        ),
        migrations.RemoveField(
            model_name='products',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='products',
            name='status',
        ),
        migrations.RemoveField(
            model_name='products',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение'),
        ),
        migrations.AlterModelTable(
            name='products',
            table='product',
        ),
    ]
