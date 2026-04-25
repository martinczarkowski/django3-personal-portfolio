from django.contrib import admin
from .models import Project, Messages

class MessagesAdmin(admin.ModelAdmin):
    readonly_field = ('created',)

admin.site.register(Project)
admin.site.register(Messages, MessagesAdmin)


