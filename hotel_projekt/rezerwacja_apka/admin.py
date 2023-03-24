from django.contrib import admin

# Register your models here.


from .models import Gosc,Rezerwacja,Pokoj

admin.site.register(Gosc)
admin.site.register(Rezerwacja)
admin.site.register(Pokoj)
