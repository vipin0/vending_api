# Generated by Django 3.2.4 on 2021-06-05 11:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210605_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.UUIDField(default=uuid.uuid5, primary_key=True, serialize=False),
        ),
    ]
