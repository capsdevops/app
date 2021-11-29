from django.db import models


class Denuncia(models.Model):
    subject = models.CharField("Caso", max_length=255)
    message = models.TextField("Descrição do Caso",)
    fotos = models.ImageField("Enviar Arquivo", upload_to='block/fotos/', blank=True)
    #blockchain = models.CharField(type="hidden")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message