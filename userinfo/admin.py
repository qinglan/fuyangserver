from django.contrib import admin

# Register your models here.


from .models import VideoCurriculumOrder, VideoInfoStudyFuyangOrder, VideoInfoLectureOrder


class VideoCurriculumOrderAdmin(admin.ModelAdmin):
    def buy_user(self, obj):
        return obj.purchaser.nickname+'-'+obj.video_curriculum.name

    list_display = ('buy_user', 'purchaser','apply_bill','price','register_date')
    ordering = ('-purchaser',)
    search_fields = ('purchaser__nickname',)


class VideoInfoStudyFuyangOrderAdmin(admin.ModelAdmin):
    def buy_user(self, obj):
        return obj.purchaser.nickname + '-' + obj.video.name

    list_display = ('buy_user', 'purchaser','apply_bill','price','register_date')
    ordering = ('-purchaser',)


class VideoInfoLectureOrderAdmin(admin.ModelAdmin):
    def buy_user(self, obj):
        return obj.purchaser.nickname + '-' + obj.video.name

    list_display = ('buy_user','purchaser','apply_bill', 'price','register_date')
    ordering = ('-purchaser',)


admin.site.register(VideoInfoLectureOrder, VideoInfoLectureOrderAdmin)

admin.site.register(VideoInfoStudyFuyangOrder, VideoInfoStudyFuyangOrderAdmin)

admin.site.register(VideoCurriculumOrder, VideoCurriculumOrderAdmin)
