# Generated by Django 4.1 on 2022-08-25 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cause', '0005_successstory'),
    ]

    operations = [
        migrations.AddField(
            model_name='successstory',
            name='summery',
            field=models.TextField(default=''),
        ),
    ]
