# Generated by Django 4.2.6 on 2023-12-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datosMicros', '0003_bus_linea_buses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Micro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=20)),
                ('idhumano', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='linea',
            name='buses',
        ),
        migrations.DeleteModel(
            name='Bus',
        ),
        migrations.AddField(
            model_name='linea',
            name='micros',
            field=models.ManyToManyField(related_name='lineas', to='datosMicros.micro'),
        ),
    ]