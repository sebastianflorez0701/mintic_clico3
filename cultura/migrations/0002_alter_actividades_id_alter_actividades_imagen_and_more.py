# Generated by Django 4.1.1 on 2022-10-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='actividades',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='ciudades',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
