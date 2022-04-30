# Generated by Django 4.0.4 on 2022-04-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_id', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('total', models.FloatField()),
                ('status', models.CharField(max_length=50)),
                ('products_count', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sales',
            },
        ),
    ]
