from django.db import models
from django.utils import timezone


############ Server e Domini ########

class ServDomini(models.Model):
    data_creazione  = models.DateField(default=timezone.now)
    serv_dominio_choise = (
    ('---','---'),
    ('VPS','VPS'),
    ('dominio', 'Dominio'),
    ('server Fisico','Server Fisico'),
    ('server virtuale','Server Virtuale'),
    )
    serv_dominio = models.CharField(max_length=12, choices=serv_dominio_choise, default='1')
    indirizzo_ip = models.CharField(max_length=20, null=True, blank=True)
    nickname_serv = models.CharField(max_length=35, null=True, blank=True)
    hostname_serv = models.CharField(max_length=35, null=True, blank=True)
    user_psw = models.TextField(max_length=250, null=True, blank=True)