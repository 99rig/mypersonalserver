from django.db import models
from django.utils import timezone
from .choise import server_tipo


############ Server ########

class Server(models.Model):
    data_creazione  = models.DateField('Data Creazione',default=timezone.now)
    server_tipo = models.CharField('Tipo di Server',max_length=25,choices=server_tipo, null=True, blank=True, default='1')
    indirizzo_ip = models.CharField('Indirizzo IP',max_length=20, null=True, blank=True)
    nickname_serv = models.CharField('NickName del Server',max_length=35, null=True, blank=True)
    hostname_serv = models.CharField('Hostname del Server',max_length=35, null=True, blank=True)
    details = models.TextField('Dettagli',max_length=250, null=True, blank=True)
    abbreviazione = models.CharField('Abbreviaz. da Shell',max_length=25, null=True, blank=True)
    costo = models.CharField('Costo del Srv Mensile',max_length=25, null=True,blank=True)

    def __str__(self):
        return u'%s %s %s' % (self.server_tipo, self.hostname_serv, self.indirizzo_ip)

############ Anagrafica ########


class Anagrafica(models.Model):
    idAnagrafica = models.AutoField(primary_key=True)
    data_creazione = models.DateField(default=timezone.now)
    ragioneSociale = models.CharField(max_length=150)
    piva = models.IntegerField()
    cf = models.CharField(max_length=20)
    indirizzoLegale = models.CharField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=100)
    citta = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, verbose_name='E-mail')
    note = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return u'%s %s %s' % (self.idAnagrafica, self.nome, self.cognome)

    def __iter__(self):
        return [self.cognome,
                self.nome,
                self.telefono,
                ]


