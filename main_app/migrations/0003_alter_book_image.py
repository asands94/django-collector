# Generated by Django 5.1.4 on 2024-12-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]