from django.contrib import admin

from .models import Birthday


@admin.register(Birthday)
class PostAdmin(admin.ModelAdmin):
    list_visible = ('first_name', 'last_name', 'birthday', 'image', 'author')
    empty_value_display = 'Не задано'
