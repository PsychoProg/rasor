# Generated by Django 4.2.5 on 2023-09-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_sharelinks_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharelinks',
            name='title',
            field=models.CharField(choices=[('TELEGRAM', 'Telegram'), ('INSTAGRAM', 'Instagram'), ('TWITTER', 'Twitter'), ('GOOGLE', 'Google'), ('PINTEREST', 'Pinterest'), ('LINKEDIN', 'Linkedin'), ('YOUTUBE', 'Youtube'), ('FACEBOOK', 'Facebook')], default='TELEGRAM'),
        ),
    ]
