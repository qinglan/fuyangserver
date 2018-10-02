from django.contrib import admin

# Register your models here.

from .models import PictureTextColumn, PictureTextPaper


class PictureTextColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'id')


class PictureTextPaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(PictureTextPaper, PictureTextPaperAdmin)
admin.site.register(PictureTextColumn, PictureTextColumnAdmin)
