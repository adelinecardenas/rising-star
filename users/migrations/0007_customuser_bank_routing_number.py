# Generated by Django 3.2.7 on 2021-10-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210930_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bank_routing_number',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True),
        ),
    ]