# Generated by Django 4.2.4 on 2023-09-05 04:32

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('home', '0007_alter_companyinfo_options_alter_sharelinks_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
