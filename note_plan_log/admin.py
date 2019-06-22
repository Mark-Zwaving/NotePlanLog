from django.contrib import admin
from . models import WebUser, Plan, Log, Note

admin.site.register(WebUser)
admin.site.register(Note)
admin.site.register(Plan)
admin.site.register(Log)
