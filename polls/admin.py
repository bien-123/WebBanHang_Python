from django.contrib import admin
from .models import Choice, Question

# Register your models here.

# Hiển thị Choice, Question trong Admin
admin.sites.register(Question)
admin.sites.register(Choice)
