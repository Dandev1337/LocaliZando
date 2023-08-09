from django.db import models

class Cliente(models.Model):
    ATIVO = 'ATIVO'
    INATIVO = 'INATIVO'
    STATUS = (
        (ATIVO, 'Ativo'),
        (INATIVO, 'Inativo'),
    )

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    #status = models.CharField(max_length=3)
    endereco = models.CharField( max_length=100, null= True)
    telefone = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=254, null=True)
    status = models.CharField(max_length=10, choices=STATUS)
    pontos_fidelidade = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome


class Cargo(models.Model):

    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    salario = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    data_admissao = models.DateField()
    endereco = models.CharField( max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome