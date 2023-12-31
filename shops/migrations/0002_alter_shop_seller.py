# Generated by Django 4.1.1 on 2023-11-05 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_buyer'),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='seller',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller', to='accounts.seller'),
        ),
    ]
