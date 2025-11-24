from django.contrib import admin
from .models import FormRegistration
from .models import User

# Register your models here.
admin.site.register(FormRegistration)
admin.site.register(User)
