from django.contrib import admin

from .models import  Order, Detail


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name','id', 'order_qty')

    @admin.display()
    def customer_name(self, obj):
        return obj.customer.name
    
    @admin.display()
    def order_qty(self, obj):
        return obj.detail_set.count()

admin.site.register(Order, OrderAdmin)

admin.site.register(Detail)

# class DetailAdmin(admin.ModelAdmin):
#     list_display = ('')