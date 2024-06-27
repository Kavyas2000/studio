from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(bookings)
admin.site.register(frame_orders)
admin.site.register(gallery)
admin.site.register(contact)
admin.site.register(appoinment)
admin.site.register(designs)
admin.site.register(addframe)
admin.site.register(feedback)
admin.site.register(PasswordReset)

# ------------TRY------------

admin.site.register(Cart_Item)

