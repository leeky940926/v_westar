# Generated by Django 3.2.7 on 2021-09-13 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210913_0705'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nut',
            new_name='Nutrition',
        ),
        migrations.AlterModelTable(
            name='allergy',
            table='allergies',
        ),
        migrations.AlterModelTable(
            name='allergyproducts',
            table='allergy_products',
        ),
        migrations.AlterModelTable(
            name='images',
            table='images',
        ),
    ]
