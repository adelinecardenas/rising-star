# Generated by Django 3.2.7 on 2021-09-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210929_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='voided_check_or_direct_deposit_form',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]