from django.contrib import admin

from retail.models import Network, Product

# # Register your models here.
# admin.site.register(Network)
#
# admin.site.register(Product)

# Register your models here.

@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'supplier', 'debt', 'link_type',)
    list_filter = ('city', )
    actions = ['zero_debt']

    def zero_debt(self, request, queryset):
        queryset.update(debt=0)

    zero_debt.short_description = 'Обнулить задолженность'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_description',)
