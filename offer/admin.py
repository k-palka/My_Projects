from typing import Tuple

from django.contrib import admin
from .models import Employee, Procedure, Offert, Company, Role


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'department')
    list_filter = ('surname', 'department')
    search_fields = ('department', 'surname')
    ordering = ['surname', 'name']


admin.site.register(Employee, EmployeeAdmin)


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('numer', 'slug', 'title', 'publish', 'open', 'close', 'status')
    list_filter = ('numer', 'status', 'publish', 'open', 'close')
    search_fields = ('numer', 'status')
    raw_id_fields = ('employees',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Procedure, ProcedureAdmin)


class OffertAdmin(admin.ModelAdmin):
    list_display = ('submission', 'price', 'lead_time', 'procedure', 'updated', 'votes')


admin.site.register(Offert, OffertAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name', 'address', 'mail', 'offert')


admin.site.register(Company, CompanyAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'employee', 'roles')


admin.site.register(Role, RoleAdmin)
