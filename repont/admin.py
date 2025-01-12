from django.contrib import admin

from repont.models import Repont, Statement

class RepontAdmin(admin.ModelAdmin):
    list_display = ["name"]

class StatementAdmin(admin.ModelAdmin):
    list_display = ["repont__name","ip","state"]


# Register your models here.
admin.site.register(Repont,RepontAdmin)
admin.site.register(Statement,StatementAdmin)

