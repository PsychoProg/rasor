# Generated by Django 4.2.4 on 2023-09-02 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_pagecontent1_author_pagecontent1_title_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyinfo',
            options={'verbose_name': 'اطلاعات شرکت', 'verbose_name_plural': 'اطلاعات شرکت'},
        ),
        migrations.AlterModelOptions(
            name='sharelinks',
            options={'verbose_name': 'لینک', 'verbose_name_plural': 'لینک ها'},
        ),
    ]
