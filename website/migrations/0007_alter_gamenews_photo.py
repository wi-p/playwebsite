# Generated by Django 4.0.4 on 2023-05-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_gamenews_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamenews',
            name='photo',
            field=models.FileField(upload_to='images/uploaded/'),
        ),
    ]
