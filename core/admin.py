from django.contrib import admin
from .models import Item, Order, OrderItem, Address, Transaction ,Checkout, Refund, TrackOrder

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)

make_refund_accepted.short_description = 'Update orders to refund granted'

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
        'shipping_address',
        'transaction'
        ]
    list_display_links = ['user',
                        'shipping_address',
                        'transaction'
                               ]
    
    list_filter = ['ordered',
                   'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted'
                    ]
    
    search_fields = ['user__username', 'reference_code']
    actions =[make_refund_accepted]

class AddressAdmin(admin.ModelAdmin):
    list_display=[
        'user',
        'town_address',
        'pick_station',
        'county',
        'zip',
        'address_type',
        'default'
    ]
    list_filter=['user', 'default', 'county' ]
    search_fields=['user', 'town_address', 'pick_station', 'zip']

# Register your models here.
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Address, AddressAdmin)
admin.site.register(Transaction)
admin.site.register(Checkout)
admin.site.register(Refund)
admin.site.register(TrackOrder)