# Generated by Django 4.2.3 on 2023-07-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentchoice', '0002_remove_app_categories_remove_app_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awardee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('pictures', models.ImageField(upload_to='nominees')),
            ],
        ),
    ]
