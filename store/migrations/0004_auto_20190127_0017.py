# Generated by Django 2.1.5 on 2019-01-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_beat_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='beat_file',
            field=models.FileField(blank=True, upload_to='audio/'),
        ),
    ]
