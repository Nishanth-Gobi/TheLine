# Generated by Django 3.2.5 on 2022-01-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0006_alter_blogpost_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='snippet',
            field=models.CharField(default='Write a description for your blogpost here', max_length=255),
        ),
    ]
