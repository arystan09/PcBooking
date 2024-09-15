from django.contrib import admin
from . models import User, Club, Room, Device, Booking, Transaction, Package, Bonus

admin.site.register(User)
admin.site.register(Club)
admin.site.register(Room)
admin.site.register(Device)
admin.site.register(Booking)
admin.site.register(Transaction)
admin.site.register(Package)
admin.site.register(Bonus)