# Generated by Django 3.0.1 on 2020-02-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20200205_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='dateCreated',
            field=models.DateField(auto_now_add=True),
        ),
    ]
