# Generated by Django 5.1.1 on 2024-11-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_id',
            field=models.IntegerField(default=0),
        ),
    ]
