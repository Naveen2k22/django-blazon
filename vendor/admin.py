from django.contrib import admin
from .models import Vendor, User, Desig, DesigGrade

admin.site.register([Vendor, Desig, DesigGrade])

class UserAdmin(admin.ModelAdmin):
    list_display = ["f_name", "l_name", "email", "address"]
    search_fields = ["f_name"]

admin.site.register(User, UserAdmin)