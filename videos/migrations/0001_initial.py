# Generated by Django 2.1 on 2019-11-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=200, verbose_name='Video Name')),
                ('video_description', models.TextField(verbose_name='Video description')),
                ('video_path', models.CharField(max_length=200, verbose_name='Video Link')),
            ],
        ),
    ]
