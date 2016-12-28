from django.contrib import admin
from .models import Contacte

class ContacteAdmin(admin.ModelAdmin):
    list_display   = ('id', 'nom', 'prenom', 'ville', 'date')
    list_filter    = ('nom','ville',)
    date_hierarchy = 'date'
    ordering       = ('date', 'nom' , 'ville' )
    search_fields  = ('nom', 'prenom' , 'date' , 'telephone' , 'mail' , 'ville')


admin.site.register(Contacte , ContacteAdmin)
# Register your models here.
