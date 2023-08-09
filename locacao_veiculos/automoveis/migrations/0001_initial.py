# Generated by Django 3.2.20 on 2023-08-05 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaAutomovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModeloAutomovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automoveis.marcaautomovel')),
            ],
        ),
        migrations.CreateModel(
            name='Automovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa_automovel', models.CharField(error_messages={'unique': 'Já há um automóvel com esta placa!'}, max_length=15, unique=True)),
                ('cor', models.CharField(max_length=20)),
                ('nro_portas', models.CharField(choices=[('2', '2 Portas'), ('3', '3 Portas'), ('4', '4 Portas'), ('5', '5 Portas')], max_length=10)),
                ('tipo_combustivel', models.CharField(choices=[('Gasolina', 'Gasolina'), ('Flex', 'Flex'), ('Diesel', 'Diesel'), ('Híbrido/Elétrico', 'Híbrido/Elétrico')], max_length=50)),
                ('quilometragem', models.FloatField()),
                ('renavam', models.CharField(max_length=20, unique=True)),
                ('valor_locacao', models.FloatField()),
                ('ano', models.PositiveIntegerField()),
                ('categoria', models.CharField(choices=[('Utilitário Esportivo', 'Utilitário Esportivo'), ('Sedã', 'Sedã'), ('Conversível / Cupê', 'Conversível / Cupê'), ('Hatch', 'Hatch'), ('Picape', 'Picape'), ('Hibrido / Elétrico', 'Hibrido / Elétrico'), ('Van', 'Van'), ('Outro', 'Outro')], max_length=50)),
                ('status', models.CharField(choices=[('Disponível', 'Disponível'), ('Indisponível', 'Indisponível')], default='Disponível', max_length=12)),
                ('chassi', models.CharField(default='00000000', max_length=50, unique=True)),
                ('imagem', models.FileField(upload_to='')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automoveis.marcaautomovel')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automoveis.modeloautomovel')),
            ],
        ),
    ]
