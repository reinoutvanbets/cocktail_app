# Generated by Django 3.0.1 on 2020-02-05 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200205_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
