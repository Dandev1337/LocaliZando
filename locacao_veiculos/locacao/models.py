from django.db import models
from cliente.models import Cliente, Funcionario
from automoveis.models import Automovel

class Locacao(models.Model):
    EM_ABERTO = 'EM_ABERTO'
    FECHADA = 'FECHADA'
    DEVOLUCAO_STATUS = (
        (EM_ABERTO, 'Em Aberto'),
        (FECHADA, 'Fechada'),
    )

    data_locacao = models.DateField()
    data_devolucao = models.DateField()
    status = models.CharField(max_length=10, choices = DEVOLUCAO_STATUS)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Automovel, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Locações'

    def __str__(self):
        return self.status