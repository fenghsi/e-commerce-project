from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Seller)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Shoppingcart)
admin.site.register(Payments)
admin.site.register(Orders)
admin.site.register(Orderitem)
admin.site.register(Delivery)
admin.site.register(Reviews)
admin.site.register(ReviewsSeller)
admin.site.register(CurrentUser)
admin.site.register(History)