from django.contrib import admin

from crud_sales.core.models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'total', 'status', 'products_count', 'state',)
    search_fields = ('id',)
    list_filter = ('created_at',)
