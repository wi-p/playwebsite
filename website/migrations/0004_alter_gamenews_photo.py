# Generated by Django 4.0.4 on 2023-05-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_gamenews_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamenews',
            name='photo',
            field=models.FileField(upload_to='static/images/uploaded/'),
        ),
    ]