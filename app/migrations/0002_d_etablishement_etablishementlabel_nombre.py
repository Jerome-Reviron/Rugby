# Generated by Django 5.0.2 on 2024-02-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='d_etablishement',
            name='EtablishementLabel_Nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
