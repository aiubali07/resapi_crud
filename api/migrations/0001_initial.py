# Generated by Django 3.2.4 on 2021-06-27 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('code', models.TextField()),
            ],
        ),
    ]