# Generated by Django 4.0.4 on 2023-06-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_gamenews_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamenews',
            name='url',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
