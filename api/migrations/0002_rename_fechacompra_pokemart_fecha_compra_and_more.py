# Generated by Django 4.1.4 on 2022-12-25 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemart',
            old_name='fechaCompra',
            new_name='fecha_compra',
        ),
        migrations.RenameField(
            model_name='pokemart',
            old_name='nombreObjeto',
            new_name='nombre_objeto',
        ),
    ]
