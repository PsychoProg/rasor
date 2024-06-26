# Generated by Django 4.2.4 on 2023-08-28 10:20

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_listbox_status_news_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listbox',
            options={'ordering': ['-created_at'], 'verbose_name': 'تصویر صفحه اصلی ', 'verbose_name_plural': 'تصاویر صفحه اصلی'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'خبر', 'verbose_name_plural': 'اخبار'},
        ),
        migrations.AlterModelManagers(
            name='listbox',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='news',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
