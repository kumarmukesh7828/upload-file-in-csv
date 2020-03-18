from django.contrib import admin
from webapp.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','ip_address','message']


admin.site.register(Contact,ContactAdmin)


