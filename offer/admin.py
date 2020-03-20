from django.contrib import admin
from .models import Employee, Procedure, Offert, Role


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'department')
    list_filter = ('last_name', 'department')
    search_fields = ('department', 'last_name')
    ordering = ['last_name', 'first_name']


admin.site.register(Employee, EmployeeAdmin)


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('numer', 'title', 'publish', 'open', 'close', 'status')
    list_filter = ('numer', 'status', 'publish', 'open', 'close')
    search_fields = ('numer', 'status')
    raw_id_fields = ('employees',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Procedure, ProcedureAdmin)


class OffertAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'submission', 'company_name', 'price', 'lead_time', 'updated', 'votes')
    list_filter = ('procedure', 'company_name', 'price', 'lead_time')
    ordering = ['procedure', 'price', 'lead_time']


admin.site.register(Offert, OffertAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('procedure', 'employee', 'roles')


admin.site.register(Role, RoleAdmin)
