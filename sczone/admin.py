from django.contrib import admin
from . models import Complain,Feedback,Course,Notification

# Register your models here.
admin.site.register(Complain)
admin.site.register(Feedback)
admin.site.register(Course)
admin.site.register(Notification)

