from django.db import models
from django.utils import timezone


############ ANAGRAFICA ########

class Anagrafica(models.Model):
    data_creazione = models.DateField(default=timezone.now)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=100)
    citta = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, verbose_name='E-mail')
    note = models.TextField(max_length=500, null=True, blank=True)


    def nuovo(self):
        self.data_creazione = timezone.now()
        self.save()

    def __str__(self):
        return u'%s %s' % (self.nome ,self.cognome)



    class Meta:
        verbose_name_plural = "Aangrafiche"