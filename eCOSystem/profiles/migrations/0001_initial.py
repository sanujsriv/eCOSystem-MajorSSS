# Generated by Django 2.1.7 on 2019-04-20 08:48

from django.db import migrations, models
import djongo.models.fields
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.EmailField(max_length=254)),
                ('follower', djongo.models.fields.ArrayModelField(model_container=profiles.models.Follower)),
                ('following', djongo.models.fields.ArrayModelField(model_container=profiles.models.Following)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
