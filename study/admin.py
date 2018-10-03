from django.contrib import admin

# Register your models here.

from .models import VideoColumn, GraphicColumn, GraphicArticle, GraphicComment, VideoCurriculumFile, VideoCurriculum, \
    VideoClass, VideoCurriculumComment, DataLst, CurriculumTaskInfoJob, CurriculumTaskInfoVideo, VideoInfoStudyFuyang, \
    VideoInfoLecture, SinglePage, MianInfo, TaskLiveFile, CurriculumTaskInfoJobAnswer


class VideoColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'image', 'subcourse')


class VideoCurriculumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'intro', 'start_time', 'stop_time', \
                    'buy_time', 'plan', 'image', 'price')


class SinglePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updatetime')
    list_display_links = ('id', 'name',)


class DataListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updatetime')
    list_display_links = ('id', 'name',)


class MianInfoAdmin(admin.ModelAdmin):
    list_display = ('text_1',)


class VideoClassAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GraphicColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro')


class GraphicArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'author', 'content', \
                    'image', 'register_date', 'update_date', 'published')


class VideoCurriculumCommentAdmin(admin.ModelAdmin):
    list_display = ('message',)


class GraphicCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'ascription', 'register_date', 'update_date', 'score')


class CurriculumTaskInfoJobAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CurriculumTaskInfoVideoAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VideoInfoLectureAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro',)


class VideoInfoStudyFuyangAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro',)


class TaskLiveFileAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CurriculumTaskInfoJobAnswerAdmin(admin.ModelAdmin):
    list_display = ('job_parent', 'comment',)


admin.site.register(CurriculumTaskInfoJobAnswer, CurriculumTaskInfoJobAnswerAdmin)

admin.site.register(TaskLiveFile, TaskLiveFileAdmin)

admin.site.register(VideoClass, VideoClassAdmin)

admin.site.register(VideoCurriculumComment, VideoCurriculumCommentAdmin)

admin.site.register(CurriculumTaskInfoJob, CurriculumTaskInfoJobAdmin)

admin.site.register(CurriculumTaskInfoVideo, CurriculumTaskInfoVideoAdmin)

admin.site.register(VideoInfoLecture, VideoInfoLectureAdmin)

admin.site.register(VideoInfoStudyFuyang, VideoInfoStudyFuyangAdmin)

admin.site.register(VideoCurriculum, VideoCurriculumAdmin)

admin.site.register(MianInfo, MianInfoAdmin)

admin.site.register(SinglePage, SinglePageAdmin)
admin.site.register(DataLst, DataListAdmin)


'''admin.site.unregister(MianInfo)

admin.site.unregister(VideoCurriculumFile)

admin.site.unregister(VideoClass)

admin.site.unregister(GraphicColumn)

admin.site.unregister(GraphicArticle)

admin.site.unregister(AdvertisingBanners)

admin.site.unregister(VideoCurriculumComment)

admin.site.unregister(GraphicComment)

admin.site.unregister(CurriculumTaskInfoJob)

admin.site.unregister(CurriculumTaskInfoVideo)

admin.site.unregister(VideoInfoLecture)

admin.site.unregister(VideoInfoStudyFuyang)

admin.site.unregister(VideoCurriculum)'''
