# Generated by Django 2.1.7 on 2019-04-20 08:49

from django.db import migrations, models
import signin.PasswordField


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('password', signin.PasswordField.PasswordModelField(max_length=16)),
                ('repeat_password', signin.PasswordField.PasswordModelField(max_length=16)),
            ],
        ),
    ]
