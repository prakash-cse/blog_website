# Generated by Django 5.1 on 2024-09-23 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='table1',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogapp.category'),
            preserve_default=False,
        ),
    ]
