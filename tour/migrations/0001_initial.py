# Generated by Django 4.1.5 on 2023-01-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '旅遊行程',
                'verbose_name_plural': '旅遊行程',
            },
        ),
    ]
