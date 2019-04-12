from django.contrib import admin

# Register your models here.


from .models import VideoCurriculumOrder, VideoInfoStudyFuyangOrder, VideoInfoLectureOrder


class VideoCurriculumOrderAdmin(admin.ModelAdmin):
    def buy_user(self, obj):
        return obj.purchaser.nickname + '-' + obj.video_curriculum.name

    def paytype(self, obj):
        if obj.video_curriculum.pay_type == '0':
            return '免费'
        elif obj.video_curriculum.pay_type == '1':
            return '余额/微信'
        else:
            return '听课券'

    buy_user.short_description = '订单名称'
    paytype.short_description = '支付方式'
    list_display = ('buy_user', 'purchaser', 'apply_bill', 'paytype', 'price', 'register_date')
    ordering = ('-register_date',)
    search_fields = ('purchaser__nickname',)


class VideoInfoStudyFuyangOrderAdmin(admin.ModelAdmin):
    def buy_user(self, obj):
        return obj.purchaser.nickname + '-' + obj.video.name

    list_display = ('buy_user', 'purchaser', 'apply_bill', 'price', 'register_date')
    ordering = ('-purchaser',)


class VideoInfoLectureOrderAdmin(admin.ModelAdmin):
    def buy_user(self, obj):
        return obj.purchaser.nickname + '-' + obj.video.name

    list_display = ('buy_user', 'purchaser', 'apply_bill', 'price', 'register_date')
    search_fields = ('purchaser__nickname',)
    ordering = ('-register_date',)


admin.site.register(VideoInfoLectureOrder, VideoInfoLectureOrderAdmin)

admin.site.register(VideoInfoStudyFuyangOrder, VideoInfoStudyFuyangOrderAdmin)

admin.site.register(VideoCurriculumOrder, VideoCurriculumOrderAdmin)
