from django.db import models
from django.urls import reverse


class MarcaAutomovel(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ModeloAutomovel(models.Model):
    marca = models.ForeignKey(MarcaAutomovel, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.marca.nome} {self.nome}"
    def get_absolute_url(self):
        return reverse('modelo_detail.html', args=[str(self.id)])

class Automovel(models.Model):
    STATUS_CHOICES = (
        ('Disponível', 'Disponível'),
        ('Indisponível', 'Indisponível'),
    )
    COMBUSTIVEL_CHOICES = (
        ('Gasolina', 'Gasolina'), ('Flex', 'Flex'),
        ('Diesel', 'Diesel'), ('Híbrido/Elétrico', 'Híbrido/Elétrico'),
    )
    MARCA_CHOICES = (
        ('Mercedes - Benz', 'Mercedes - Benz'), ('Audi', 'Audi'),('BMW', 'BMW'),
        ('Volkswagen',  'Volkswagen'), ('Chevrolet', 'Chevrolet'), ('Renault', 'Renault'),
        ('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Fiat', 'Fiat'), ('Hyundai', 'Hyundai'),
        ('Peugeot', 'Peugeot'), ('Lexus', 'Lexus'), ('Kia','Kia'), ('Citroën', 'Citroën'),
        ('Nissan', 'Nissan'), ('Mitsubishi', 'Mitsubishi'), ('Chery', 'Chery'),('Jeep', 'Jeep'),
    )
    CATEGORIA_CHOICES = (
        ('Utilitário Esportivo', 'Utilitário Esportivo'),
        ('Sedã', 'Sedã'), ('Conversível / Cupê', 'Conversível / Cupê'),
        ('Hatch', 'Hatch'), ('Picape', 'Picape'), ('Hibrido / Elétrico', 'Hibrido / Elétrico'),
        ('Van','Van'), ('Outro', 'Outro'),
    )

    NRO_PORTAS_CHOICES =(
        ('2', '2 Portas'),
        ('3', '3 Portas'),
        ('4', '4 Portas'),
        ('5', '5 Portas'), # Existe!
    )
    placa_automovel = models.CharField(max_length=15, unique=True, error_messages={'unique':"Já há um automóvel com esta placa!"}, null= False)
    cor = models.CharField(max_length=20)
    nro_portas = models.CharField(max_length=10, choices=NRO_PORTAS_CHOICES, null= False)
    marca = models.ForeignKey(MarcaAutomovel, on_delete=models.CASCADE)
    tipo_combustivel = models.CharField(max_length=50, choices=COMBUSTIVEL_CHOICES, null= False)
    quilometragem= models.FloatField()
    renavam= models.CharField(max_length=20, unique=True)
    valor_locacao = models.FloatField()
    modelo = models.ForeignKey(ModeloAutomovel, on_delete=models.CASCADE)
    ano = models.PositiveIntegerField()
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=50, null= False)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Disponível')
    chassi = models.CharField(max_length=50, unique=True, default= '00000000')
    imagem = models.FileField(upload_to="")


    def __str__(self):
        carro = self.marca.nome + ' ' + self.modelo.nome + ' ' + str(self.ano) + ' - '
        carro += self.placa_automovel + ' -- Diária padrão R$ ' + str(self.valor_locacao)
        return carro

