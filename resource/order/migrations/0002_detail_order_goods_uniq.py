# Generated by Django 4.2.2 on 2023-06-26 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='detail',
            constraint=models.UniqueConstraint(fields=('order', 'goods'), name='order_goods_uniq'),
        ),
    ]