# Generated by Django 5.0.2 on 2024-02-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_club_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='code_commune',
            field=models.CharField(max_length=255),
        ),
    ]
