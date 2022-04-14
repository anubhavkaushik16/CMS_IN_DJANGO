# Generated by Django 4.0.4 on 2022-04-14 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('phno', models.CharField(max_length=20)),
                ('image', models.ImageField(default='images/default.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]