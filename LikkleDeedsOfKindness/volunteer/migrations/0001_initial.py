# Generated by Django 4.0.3 on 2022-03-20 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cause', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=60)),
                ('phone_number', models.CharField(max_length=20)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cause.event')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='AdminVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.volunteer')),
            ],
        ),
    ]