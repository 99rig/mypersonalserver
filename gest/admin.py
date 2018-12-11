from django.contrib import admin
from .models import ServDomini

class ServDominiAdmin(admin.ModelAdmin):
    list_display = ("serv_dominio","indirizzo_ip",'nickname_serv','hostname_serv','user_psw',)
    fieldsets = [
        ('Server', {
            'fields': ['serv_dominio', 'indirizzo_ip','nickname_serv','hostname_serv','user_psw']
        }),
    ]


admin.site.register(ServDomini,ServDominiAdmin)
