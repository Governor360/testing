# Generated by Django 4.2.3 on 2023-07-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentchoice', '0009_remove_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(upload_to='pix'),
        ),
    ]