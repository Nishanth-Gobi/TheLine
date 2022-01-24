# Generated by Django 3.2.5 on 2022-01-24 00:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_remove_blogpost_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
