# Generated by Django 5.0.2 on 2024-02-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_club_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d_club',
            name='code_commune',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='d_club',
            name='code_qpv',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
