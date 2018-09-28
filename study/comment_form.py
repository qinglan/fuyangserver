# coding:utf-8


from django import forms


class VideoCurriculumCommentForm(forms.Form):
    content = forms.CharField()
    score = forms.IntegerField()


class VideoInfoLectureCommentForm(forms.Form):
    content = forms.CharField()


class VideoInfoStudyFuyangCommentForm(forms.Form):
    content = forms.CharField()

