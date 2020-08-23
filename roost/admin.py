from django.contrib import admin
from .models import PreSchedule, User, Organisation
# Register your models here.
admin.site.register(PreSchedule)
admin.site.register(User)
admin.site.register(Organisation)