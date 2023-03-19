# Generated by Django 3.2.9 on 2022-01-06 19:05

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_convert_to_valid_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineattribute',
            name='value',
            field=models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, verbose_name='Value'),
        ),
    ]
