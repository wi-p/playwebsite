# Generated by Django 4.0.4 on 2023-04-28 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_foundation', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GameStationHasGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TypeGameStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_foundation', models.DateField()),
                ('description', models.TextField()),
                ('game_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.gamecompany')),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_foundation', models.DateField()),
                ('description', models.TextField()),
                ('game_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.gamecompany')),
                ('game_station', models.ManyToManyField(through='website.GameStationHasGame', to='website.typegamestation')),
            ],
        ),
        migrations.AddField(
            model_name='gamestationhasgame',
            name='game_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.typegamestation'),
        ),
        migrations.AddField(
            model_name='gamestationhasgame',
            name='video_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.videogame'),
        ),
    ]
