# Generated by Django 4.2.3 on 2023-07-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentchoice', '0010_alter_category_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(upload_to='nominees'),
        ),
    ]
