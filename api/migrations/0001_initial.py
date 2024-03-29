# Generated by Django 3.2.9 on 2021-11-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShahidModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='shahids/')),
                ('born_date', models.DateTimeField()),
                ('shahadat_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'شهید',
                'verbose_name_plural': 'شهدا',
            },
        ),
    ]
