# Generated by Django 3.0.3 on 2020-06-28 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='blog_pics'),
        ),
    ]