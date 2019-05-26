from django.contrib import admin

# Register your models here.
from foodtaskerapp.models import Restaurant, Driver, Customer

admin.site.register(Restaurant)
admin.site.register(Driver)
admin.site.register(Customer)
