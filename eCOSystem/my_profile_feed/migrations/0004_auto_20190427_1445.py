# Generated by Django 2.1.7 on 2019-04-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile_feed', '0003_user_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_portfolio',
            name='user_portfolio',
            field=models.FileField(blank=True, upload_to='profile_docs/%Y/%m/%d'),
        ),
    ]
