# Generated by Django 4.2.5 on 2023-09-11 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]