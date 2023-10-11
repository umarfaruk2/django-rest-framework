from django.contrib import admin
from .models import StudentApiViewModel
# Register your models here.

@admin.register(StudentApiViewModel)
class StudentApiViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']



