from django.contrib import admin

# Register your models here.

from .models import PictureTextColumn, PictureTextPaper


class PictureTextColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')


class PictureTextPaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','column')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(PictureTextPaper, PictureTextPaperAdmin)
admin.site.register(PictureTextColumn, PictureTextColumnAdmin)
