from django.db import models
from django.core.validators import MinLengthValidator

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.IntegerField()
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):                    
        return self.nome   
    
class Professor(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    cref = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Aula(models.Model):
    nome = models.CharField(max_length=20)
    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL, null=True,
        related_name='aula'
    )
    sala = models.ForeignKey(
        Sala,
        on_delete=models.SET_NULL, null=True,
        related_name='aula'
    )

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    aula = models.ForeignKey(
        Aula,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )

    def __str__(self):
        return f'{self.aluno} - {self.aula}'