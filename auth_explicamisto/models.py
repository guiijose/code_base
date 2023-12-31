from django.db import models
from django.contrib.auth.models import AbstractUser

class Cursos(models.Model):
    nome = models.CharField(max_length=75)
class Faculdade(models.Model):
    faculdade_nome = models.CharField(max_length=150, blank=False)
    cursos = models.ManyToManyField(Cursos, blank=True )
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    faculdade = models.ManyToManyField(Faculdade)
    explicador = models.BooleanField(default=False)
    exame_este_ano = models.BooleanField(default=False)
class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    explicandos = models.ManyToManyField(User, blank=True, related_name='subjects_explicandos')
    explicadores = models.ManyToManyField(User, blank=True, related_name='subjects_explicadores')

    exame_obrigatorio = models.BooleanField()

