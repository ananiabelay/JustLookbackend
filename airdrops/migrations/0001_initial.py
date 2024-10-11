# Generated by Django 5.1.1 on 2024-10-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airdrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('listing_date', models.DateField(blank=True, null=True)),
                ('overview', models.TextField()),
                ('qualification', models.TextField()),
                ('farming_ending_date', models.DateField(blank=True, null=True)),
                ('whitepaper', models.URLField(blank=True)),
                ('total_supply', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('supply_for_airdrop', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('starting_link', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='airdrops/')),
            ],
        ),
    ]
