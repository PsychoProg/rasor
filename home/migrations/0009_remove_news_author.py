# Generated by Django 4.2.4 on 2023-09-05 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_news_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
    ]
