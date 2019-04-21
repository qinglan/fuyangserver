from django.contrib import admin
from .models import AdvertisingBanners, VideoInfoLectureBanners, VideoInfoStudyFuyangBanners,VideoAlternateBanners,VideoInnerAdBanners


# Register your models here.

class AdvertisingBannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url')


class VideoInfoLectureBannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url')


class VideoAlternateBannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url')


class VideoInnerAdBannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url' , 'location')


class VideoInfoStudyFuyangBannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url')


admin.site.register(AdvertisingBanners, AdvertisingBannersAdmin)

admin.site.register(VideoInfoLectureBanners, VideoInfoLectureBannersAdmin)

admin.site.register(VideoInfoStudyFuyangBanners, VideoInfoStudyFuyangBannersAdmin)

admin.site.register(VideoAlternateBanners, VideoAlternateBannersAdmin)

admin.site.register(VideoInnerAdBanners, VideoInnerAdBannersAdmin)
