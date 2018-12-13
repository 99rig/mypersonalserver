from django.contrib import admin
from .models import Server, Anagrafica

class ServerAdmin(admin.ModelAdmin):
    list_display = ("server_tipo",'fornitore',"indirizzo_ip",'nickname_serv','hostname_serv','abbreviazione',)
    fieldsets = [
        ('Server', {
            'fields': ['fornitore','server_tipo', 'indirizzo_ip','nickname_serv','hostname_serv','abbreviazione','details',]
        }),
    ]


admin.site.register(Server,ServerAdmin)


class AnagraficaAdmin(admin.ModelAdmin):
    list_display =('ragioneSociale','piva','cf','email')
    fieldsets = [
        ('Anagrafica', {
            'fields': ['ragioneSociale','piva','cf','indirizzoLegale','nome','cognome','indirizzo','citta','email','telefono','note']
        }
         )

    ]

admin.site.register(Anagrafica,AnagraficaAdmin)
