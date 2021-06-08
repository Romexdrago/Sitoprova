from django.db import models
# Create your models here.
class Pizze(models.Model):
    nome=models.CharField(max_length=30)
    ingredienti=models.TextField()
    prezzo=models.CharField(max_length=10)
    immagine = models.ImageField(max_length=150, blank=True, null=True)
    class Meta:
        verbose_name="Pizza"
        verbose_name_plural="Pizze"
    def __str__(self):
        return self.nome
