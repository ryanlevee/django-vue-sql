from django.contrib import admin

from .models import Applicant, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['title', 'created', 'updated', 'id']
    list_filter = ['title']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated')
        return ()


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    model = Applicant
    list_display = ['first_name', 'last_name', 'job',
                    'created', 'updated', 'id']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated')
        return ()