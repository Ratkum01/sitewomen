# Generated by Django 4.2.5 on 2023-11-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0010_alter_category_options_alter_women_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
    ]
