# Generated by Django 4.2.5 on 2023-10-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='women',
            index=models.Index(fields=['time_create'], name='women_women_time_cr_21b781_idx'),
        ),
    ]
