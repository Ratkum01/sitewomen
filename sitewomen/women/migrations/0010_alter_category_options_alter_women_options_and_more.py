# Generated by Django 4.2.5 on 2023-11-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0009_husband_women_husband'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create'], 'verbose_name': 'Известный У', 'verbose_name_plural': 'Известные Ж'},
        ),
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255, verbose_name='НАЗВАНИЕ ЧЕ ТАМ ?'),
        ),
    ]
