# Generated by Django 3.0.8 on 2020-07-25 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('street_trees_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RK_Ashram_marg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Tree_code', models.CharField(error_messages={'unique': 'The Tree code you have entered is already exists.'}, max_length=8, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('common_name', models.CharField(max_length=45)),
                ('scientific_name', models.CharField(max_length=45)),
                ('Age', models.IntegerField()),
                ('Height', models.FloatField()),
                ('Diameter_girth', models.FloatField()),
                ('closest_address', models.CharField(max_length=45)),
                ('Longitude', models.DecimalField(decimal_places=6, error_messages={'unique': 'Longitude value already exists'}, max_digits=8, unique=True)),
                ('Latitude', models.DecimalField(decimal_places=6, error_messages={'unique': 'Latitude value already exists'}, max_digits=8, unique=True)),
                ('specie_code', models.CharField(max_length=8)),
                ('condition', models.CharField(max_length=45)),
            ],
        ),
    ]
