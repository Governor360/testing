# Generated by Django 4.2.3 on 2023-07-20 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentchoice', '0014_delete_pictures_category_details_category_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinfo',
            name='carousel4',
            field=models.ImageField(null=True, upload_to='carousel'),
        ),
        migrations.AddField(
            model_name='appinfo',
            name='carousel5',
            field=models.ImageField(null=True, upload_to='carousel'),
        ),
    ]
