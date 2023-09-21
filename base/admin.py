from django.contrib import admin
from .models import Profile, HomePage, Contact, Live_Chat

# Register your models here.
admin.site.register(Profile)
admin.site.register(HomePage)
admin.site.register(Contact)
admin.site.register(Live_Chat)