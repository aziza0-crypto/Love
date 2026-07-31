from django.contrib import admin

# Register your models here.
from .models import Student


admin.site.register(Student)

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "email",
        "created_at"
    )
