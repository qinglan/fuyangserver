from django.contrib import admin

# Register your models here.

from .models import PictureTextColumn, PictureTextPaper, PictureTextPaperComment


class PictureTextColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')


class PictureTextPaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'column')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class PictureTextPaperCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'ascription', 'register_date', 'author')
    list_display_links = ('id', 'message')

    list_filter = ('author',)
    search_fields = ('message',)
    date_hierarchy = 'register_date'
    ordering = ('-register_date',)
    readonly_fields = ('message', 'ascription', 'register_date', 'author')
    list_per_page = 20

    def has_add_permission(self, request):
        '隐藏添加按钮'
        return False


admin.site.register(PictureTextPaper, PictureTextPaperAdmin)
admin.site.register(PictureTextColumn, PictureTextColumnAdmin)
admin.site.register(PictureTextPaperComment, PictureTextPaperCommentAdmin)

admin.AdminSite.site_title = '扶阳医学'
admin.AdminSite.site_header = '火神门'
