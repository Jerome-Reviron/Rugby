# Generated by Django 5.0.2 on 2024-02-12 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_d_agegrp_d_commune_d_geopostion_d_qpv_d_sex_f_club'),
    ]

    operations = [
        migrations.RenameField(
            model_name='d_qpv',
            old_name='code',
            new_name='code_qpv',
        ),
    ]
