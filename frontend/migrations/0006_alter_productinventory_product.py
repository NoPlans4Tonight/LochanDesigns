# Generated by Django 4.0.6 on 2022-10-18 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_alter_productinventory_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.product'),
        ),
    ]
