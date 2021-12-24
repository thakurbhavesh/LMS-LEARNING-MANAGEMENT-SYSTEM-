from django.contrib import admin
from .models import Customer,Image,AdminLogin,File
# Register your models here.
admin.site.register(Customer)
admin.site.register(Image)
admin.site.register(AdminLogin)
admin.site.register(File)