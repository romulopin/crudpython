from django.db import models


# Create your models here.

class Cliente(models.Model):
        nome = models.CharField(max_length=100)
        apelido = models.CharField(max_length=100)
        cpf = models.CharField('CPF', max_length=11, unique=True)
        idade = models.IntegerField()
        email = models.EmailField(unique=True)
        telefone = models.CharField(max_length=20, blank=True)
        criado_em = models.DateTimeField('criado em', auto_now_add=True)

        def __str__(self):
            return self.nome

class Produto(models.Model):
        nome = models.CharField(max_length=100)
        preco = models.FloatField(null=False)

        def __str__(self):
            return self.nome

class Vendedor(models.Model):
        nome = models.CharField(max_length=100)
        cpf = models.CharField('CPF', max_length=11, unique=True)
        #comissao = models.IntegerField()
        produto_vendido = models.ManyToManyField(Produto)

        def __str__(self):
            return self.nome
