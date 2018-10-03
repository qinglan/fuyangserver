from django.contrib import admin
from .models import AdvertisingBanners, VideoInfoLectureBanners, VideoInfoStudyFuyangBanners


# Register your models here.

class AdvertisingBannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url')


class VideoInfoLectureBannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url')


class VideoInfoStudyFuyangBannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url')


admin.site.register(AdvertisingBanners, AdvertisingBannersAdmin)

admin.site.register(VideoInfoLectureBanners, VideoInfoLectureBannersAdmin)

admin.site.register(VideoInfoStudyFuyangBanners, VideoInfoStudyFuyangBannersAdmin)
