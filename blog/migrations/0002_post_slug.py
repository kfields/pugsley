# Generated by Django 2.1.7 on 2019-04-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='my-first-post', unique=True),
            preserve_default=False,
        ),
    ]
