# Generated by Django 4.2.3 on 2023-07-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentchoice', '0006_appinfo_delete_app_delete_awardee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='nominees')),
                ('details', models.CharField(max_length=50)),
            ],
        ),
    ]
