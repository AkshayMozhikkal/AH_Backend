# Generated by Django 4.2.5 on 2023-10-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0011_alter_address_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='uuser',
            name='art',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
