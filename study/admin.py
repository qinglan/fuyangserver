from django.contrib import admin

# Register your models here.

from .models import VideoColumn, VideoInfoLectureDetails, GraphicArticle, GraphicComment, VideoCurriculumFile, \
    VideoCurriculum, \
    VideoClass, VideoCurriculumComment, DataLst, CurriculumTaskInfoJob, CurriculumTaskInfoVideo, VideoInfoStudyFuyang, \
    VideoInfoLecture, VideoInfoLectureComment, SinglePage, MianInfo, TaskLiveFile, TaskInfoVideoComment, \
    CurriculumTaskInfoJobAnswer, VideoInfoLectureClassfy, VideoVipPrice


class VideoColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'image', 'subcourse')


class VideoCurriculumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'intro', 'start_time', 'stop_time',
                    'buy_time', 'plan', 'image', 'price')
    list_display_links = ('id', 'name')


class SinglePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updatetime')
    list_display_links = ('id', 'name',)


class DataListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updatetime')
    list_display_links = ('id', 'name',)


class MianInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'text_1',)


class VideoClassAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GraphicColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro')


class GraphicArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'author', 'content', \
                    'image', 'register_date', 'update_date', 'published')


class VideoCurriculumCommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'register_date', 'author')
    list_per_page = 30
    list_filter = ('author',)
    search_fields = ('message',)
    date_hierarchy = 'register_date'

    readonly_fields = ('message', 'ascription', 'register_date', 'author')

    def has_add_permission(self, request):
        return False


class VideoInfoLectureCommentAdmin(admin.ModelAdmin):
    '视频区评论'
    list_display = ('message', 'register_date', 'author')
    list_per_page = 30
    list_filter = ('author',)
    search_fields = ('message',)
    date_hierarchy = 'register_date'

    readonly_fields = ('message', 'ascription', 'register_date', 'author')

    def has_add_permission(self, request):
        return False


class TaskInfoVideoCommentAdmin(admin.ModelAdmin):
    '视频直播评论'
    list_display = ('message', 'register_date', 'author')
    list_per_page = 30
    list_filter = ('author',)
    search_fields = ('message',)
    date_hierarchy = 'register_date'

    readonly_fields = ('message', 'ascription', 'register_date', 'author')

    def has_add_permission(self, request):
        return False


class GraphicCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'ascription', 'register_date', 'update_date', 'score')


class CurriculumTaskInfoJobAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CurriculumTaskInfoVideoAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VideoInfoLectureInline(admin.TabularInline):
    model = VideoInfoLectureDetails
    extra = 0  # 默认不显示新增


class VideoInfoLectureAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro',)
    exclude = ('play_id', 'play_app_id')  # 屏蔽录播文件id
    inlines = [VideoInfoLectureInline]


class VideoInfoStudyFuyangAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro',)


class TaskLiveFileAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CurriculumTaskInfoJobAnswerAdmin(admin.ModelAdmin):
    list_display = ('job_parent', 'comment',)


class VideoInfoLectureClassfyAdmin(admin.ModelAdmin):
    list_display = ('message', 'remark', 'register_date')


class VideoVipPriceAdmin(admin.ModelAdmin):
    list_display = ('VIP_price', 'min_exchange_ticket_price')

    def has_add_permission(self, request, obj=None):
        '禁止新增'
        return False

    def has_delete_permission(self, request, obj=None):
        '禁止删除'
        return False


admin.site.register(VideoInfoLectureClassfy, VideoInfoLectureClassfyAdmin)
admin.site.register(CurriculumTaskInfoJobAnswer, CurriculumTaskInfoJobAnswerAdmin)
admin.site.register(TaskLiveFile, TaskLiveFileAdmin)
admin.site.register(VideoClass, VideoClassAdmin)
admin.site.register(VideoCurriculumComment, VideoCurriculumCommentAdmin)
admin.site.register(CurriculumTaskInfoJob, CurriculumTaskInfoJobAdmin)
admin.site.register(CurriculumTaskInfoVideo, CurriculumTaskInfoVideoAdmin)
admin.site.register(VideoInfoLecture, VideoInfoLectureAdmin)
# admin.site.register(VideoInfoStudyFuyang, VideoInfoStudyFuyangAdmin)
admin.site.register(VideoCurriculum, VideoCurriculumAdmin)
admin.site.register(VideoInfoLectureComment, VideoInfoLectureCommentAdmin)
admin.site.register(MianInfo, MianInfoAdmin)
admin.site.register(SinglePage, SinglePageAdmin)
admin.site.register(DataLst, DataListAdmin)
admin.site.register(TaskInfoVideoComment, TaskInfoVideoCommentAdmin)
admin.site.register(VideoVipPrice, VideoVipPriceAdmin)
