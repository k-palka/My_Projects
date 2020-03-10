from django.contrib import admin
from .models import Employee, Procedure, Offert, Company


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'department', 'role')
    list_filter = ('surname', 'department', 'role')
    search_fields = ('department', 'role')
    ordering = ['surname', 'role']


admin.site.register(Employee, EmployeeAdmin)

admin.site.register(Procedure)
admin.site.register(Offert)
admin.site.register(Company)
