# Generated by Django 3.2 on 2021-10-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=100)),
                ('github_url', models.URLField()),
                ('live_url', models.URLField()),
            ],
        ),
    ]
