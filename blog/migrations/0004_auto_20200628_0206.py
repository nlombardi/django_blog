# Generated by Django 3.0.3 on 2020-06-28 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200628_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='blog_pics'),
        ),
    ]
