# Generated by Django 3.2.19 on 2023-06-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20230602_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='forecast_pxp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
