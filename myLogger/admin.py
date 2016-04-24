from django.contrib import admin

# Register your models here.
from myLogger.models import myLogger


class myLoggerAdmin(admin.ModelAdmin):
    model = myLogger

admin.site.register(myLogger, myLoggerAdmin)