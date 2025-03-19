# Generated by Django 5.1.3 on 2024-12-14 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_author_name_author_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='author',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
