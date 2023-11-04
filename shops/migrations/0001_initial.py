# Generated by Django 4.2.7 on 2023-11-04 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(choices=[('A', 'catagory a'), ('B', 'catagory b'), ('C', 'catagory c')], max_length=100)),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='seller', to='accounts.seller')),
            ],
        ),
    ]