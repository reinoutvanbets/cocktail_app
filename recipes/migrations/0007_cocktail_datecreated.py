# Generated by Django 3.0.1 on 2020-02-05 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20200205_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='dateCreated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
