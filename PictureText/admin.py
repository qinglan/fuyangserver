from django.contrib import admin

# Register your models here.

from .models import PictureTextColumn, PictureTextColumn1, PictureTextColumn2, PictureTextColumn3, PictureTextColumn4, \
    PictureTextPaper, PictureTextPaper1, PictureTextPaper2, PictureTextPaper3, PictureTextPaper4

class PictureTextColumnAdmin(admin.ModelAdmin):
    list_display = ('name','id')

class PictureTextPaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(PictureTextPaper, PictureTextPaperAdmin)
admin.site.register(PictureTextPaper1, PictureTextPaperAdmin)
admin.site.register(PictureTextPaper2, PictureTextPaperAdmin)
admin.site.register(PictureTextPaper3, PictureTextPaperAdmin)
admin.site.register(PictureTextPaper4, PictureTextPaperAdmin)

admin.site.register(PictureTextColumn, PictureTextColumnAdmin)
admin.site.register(PictureTextColumn1, PictureTextColumnAdmin)
admin.site.register(PictureTextColumn2, PictureTextColumnAdmin)
admin.site.register(PictureTextColumn3, PictureTextColumnAdmin)
admin.site.register(PictureTextColumn4, PictureTextColumnAdmin)