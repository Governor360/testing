# Generated by Django 4.2.3 on 2023-07-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentchoice', '0005_awardee_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('carousel1', models.ImageField(upload_to='carousel')),
                ('carousel2', models.ImageField(upload_to='carousel')),
                ('carousel3', models.ImageField(upload_to='carousel')),
                ('logo', models.ImageField(upload_to='logo')),
                ('copyright', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='App',
        ),
        migrations.DeleteModel(
            name='Awardee',
        ),
    ]
