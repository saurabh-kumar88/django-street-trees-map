# Generated by Django 3.0.8 on 2020-07-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mandir_marg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Tree_code', models.CharField(max_length=8)),
                ('common_name', models.CharField(max_length=45)),
            ],
        ),
    ]
