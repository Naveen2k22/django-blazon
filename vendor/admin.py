from django.contrib import admin
from .models import Vendor, User

admin.site.register(Vendor)

class UserAdmin(admin.ModelAdmin):
    list_display = ["f_name", "l_name", "email", "address"]
    search_fields = ["f_name"]

admin.site.register(User, UserAdmin)