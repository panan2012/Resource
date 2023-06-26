from django.contrib import admin

from .models import  Order, Detail


class DetailInline(admin.TabularInline):
    model = Detail
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name','id', 'order_qty', 'order_sum')
    inlines = [
        DetailInline,
    ]

    @admin.display()
    def customer_name(self, obj):
        return obj.customer.name
    
    @admin.display()
    def order_qty(self, obj):
        return obj.detail_set.count()
    
    @admin.display()
    def order_sum(self, obj):
        return sum(obj.detail_set.values_list('total', flat=True))

admin.site.register(Order, OrderAdmin)
