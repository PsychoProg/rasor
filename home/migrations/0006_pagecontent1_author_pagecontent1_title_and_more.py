# Generated by Django 4.2.4 on 2023-08-31 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontent1',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagecontent1',
            name='title',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='pagecontent2',
            name='title',
            field=models.CharField(blank=True, max_length=155, null=True),
        ),
    ]
