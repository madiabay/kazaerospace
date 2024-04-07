from django.contrib import admin
from . import models


fields = (
    'id',
    'familia',
    'imya',
    'otchestvo',
    'email',
    'phone_number',
    'date_of_birth',
    'sex',
    'user_role',
)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'email',)
    fieldsets = (
        (None, {'fields': fields}),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(models.CustomUser, CustomUserAdmin)
