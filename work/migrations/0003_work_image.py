# Generated by Django 3.0.1 on 2020-01-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_remove_work_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
