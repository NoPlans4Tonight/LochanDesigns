# Generated by Django 4.0.6 on 2022-10-17 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinventory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='frontend.product'),
        ),
    ]
