from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Customer, CustomerAdmin)

