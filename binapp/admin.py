from django.contrib import admin

# Register your models here.
from binapp import models

admin.site.register(models.Login)
admin.site.register(models.driver)
admin.site.register(models.Customer)
admin.site.register(models.complaint)
admin.site.register(models.Complaintdriver)
admin.site.register(models.Notification)
# admin.site.register(models.Binrequest)
admin.site.register(models.Garbage)
