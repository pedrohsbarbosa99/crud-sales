# Generated by Django 4.0.4 on 2022-05-01 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_sale_id_alter_sale_sale_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='sale_id',
            new_name='id',
        ),
    ]
