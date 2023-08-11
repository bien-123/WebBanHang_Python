from django.contrib import admin
from .models import Choice, Question

# Register your models here.

# Hiển thị Choice, Question trong Admin
admin.site.register(Question)
admin.site.register(Choice)
