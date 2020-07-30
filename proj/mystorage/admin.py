from django.contrib import admin
# Register your models here.
from mystorage.models import Essay, UserData, Lead

admin.site.register(Essay)
admin.site.register(UserData)
admin.site.register(Lead)