# Generated by Django 4.0.3 on 2022-05-25 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_projectimages_projectimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video_link',
            field=models.CharField(default='none', max_length=225),
        ),
    ]
