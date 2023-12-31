# Generated by Django 4.2.4 on 2023-08-16 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conso', '0002_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nom de la variable')),
                ('unite_mesure', models.CharField(blank=True, max_length=100, null=True, verbose_name='Unité de mesure de la variable')),
            ],
        ),
        migrations.CreateModel(
            name='Dispositif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_lieu', models.CharField(blank=True, max_length=100, null=True, verbose_name='Le lieu où se trouve le dispositif')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.FloatField()),
                ('precision', models.FloatField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conso.section')),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conso.variable')),
            ],
        ),
        migrations.CreateModel(
            name='Consommation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.FloatField()),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('dispositif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conso.dispositif')),
            ],
        ),
    ]
