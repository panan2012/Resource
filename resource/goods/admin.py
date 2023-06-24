from django.contrib import admin

from .models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost')


admin.site.register(Goods, GoodsAdmin)
