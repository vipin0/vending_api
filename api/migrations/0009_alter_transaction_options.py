# Generated by Django 3.2.4 on 2021-06-07 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_transaction_billed_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-timestamp']},
        ),
    ]
