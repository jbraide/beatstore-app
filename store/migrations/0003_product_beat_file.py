# Generated by Django 2.1.5 on 2019-01-26 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='beat_file',
            field=models.FileField(blank=True, upload_to='static/audio'),
        ),
    ]