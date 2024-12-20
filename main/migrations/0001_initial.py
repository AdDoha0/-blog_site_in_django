# Generated by Django 4.2 on 2024-11-03 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, verbose_name='Текст статьи')),
                ('is_published', models.BooleanField(db_index=True, default=False, verbose_name='Статус')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='main.category', verbose_name='Категории')),
            ],
        ),
    ]
