from django.contrib import admin
from .models import Dispensary


class DispensaryAdmin(admin.ModelAdmin):
    list_display = [ "business_name", "dba", "street_address", "city", ]


admin.site.register(Dispensary)


