# Generated by Django 4.1.7 on 2023-03-31 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
