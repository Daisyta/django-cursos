from django.db import models

# Create your models here.

#validaciones,aqui configuro que mensajes le doy al usuario si comete un error o fue exitoso lo que hizo
class CursoManager(models.Manager):

    def validaciones(self,postData):
        errors = {}

        if len(postData['Name']) < 2:
            errors['len_Name'] = "El campo name debe tener al menos 2 caracteres"
        return errors

#modelo
class Curso(models.Model):

    Name = models.CharField(max_length=155)
    Description = models.CharField(max_length=255)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now= True)


    objects = CursoManager()


    def __str__(self):
        return f"{self.Name}"

    def __repr__(self):
        return f"{self.Name}"
    