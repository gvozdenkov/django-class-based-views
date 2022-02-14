from csv import list_dialects
from django.contrib import admin

from . models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_filter = ("username",)
    list_display = ("username", "message")


admin.site.register(Message, MessageAdmin)