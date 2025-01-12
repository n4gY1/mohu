# Generated by Django 5.1 on 2025-01-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('state', models.CharField(max_length=1)),
                ('description', models.TextField()),
            ],
        ),
    ]
