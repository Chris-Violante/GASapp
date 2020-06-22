# Generated by Django 3.0.5 on 2020-06-22 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('instrument_type', models.CharField(max_length=150)),
                ('manufacturer', models.CharField(max_length=150)),
                ('serial', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('condition', models.CharField(choices=[('U', 'Used'), ('P', 'Poor'), ('F', 'Fair'), ('G', 'Good'), ('V', 'Very Good'), ('E', 'Excellent'), ('M', 'Mint'), ('B', 'BrandNew')], default='U', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
