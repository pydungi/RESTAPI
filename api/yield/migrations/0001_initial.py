# Generated by Django 4.1.1 on 2022-12-26 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yield',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('yield_corn', models.IntegerField()),
            ],
            options={
                'db_table': 'yield_data',
            },
        ),
    ]
