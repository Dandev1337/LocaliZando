# Generated by Django 3.2.20 on 2023-08-07 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('automoveis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_locacao', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('status', models.CharField(choices=[('EM_ABERTO', 'Em Aberto'), ('FECHADA', 'Fechada')], max_length=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.funcionario')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automoveis.automovel')),
            ],
            options={
                'verbose_name_plural': 'Locações',
            },
        ),
    ]