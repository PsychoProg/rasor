# Generated by Django 4.2.5 on 2023-09-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_orderitem_course_alter_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product_type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]