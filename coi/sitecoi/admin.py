from django.contrib import admin

from .models import Armas


class ArmasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Armas, ArmasAdmin)
