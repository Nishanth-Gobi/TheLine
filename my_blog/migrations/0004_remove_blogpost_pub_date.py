# Generated by Django 3.2.5 on 2022-01-24 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_auto_20220124_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='pub_date',
        ),
    ]