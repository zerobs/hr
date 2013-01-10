from leave.models import employees,departments
from django.contrib import admin

class employeesAdmin(admin.ModelAdmin):
    list_display = ('firstname','familyName','department')
    list_filter = ('department',)
    search_fields = ('firstname','familyName')

admin.site.register(employees,employeesAdmin)
admin.site.register(departments)
