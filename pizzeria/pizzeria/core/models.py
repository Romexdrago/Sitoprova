from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class RecensioneModel(models.Model):
    cliente=models.ForeignKey(User,on_delete=models.CASCADE,related_name="recensioni")
    contenuto=models.TextField()
    pizza_ordinata=models.CharField(max_length=30,null=True,blank=True)
    data_pubblicazione=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.contenuto
    class Meta:
        verbose_name="Recensione"
        verbose_name_plural = "Recensioni"
