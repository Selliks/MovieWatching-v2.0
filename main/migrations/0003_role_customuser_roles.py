# Generated by Django 5.1.3 on 2024-12-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_movie_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('user', 'Regular User'), ('author', 'Author'), ('admin', 'Admin')], max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='users', to='main.role'),
        ),
    ]
