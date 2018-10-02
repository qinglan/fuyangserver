from django.http import HttpResponse
from django.shortcuts import render
from .models import PictureTextColumn, PictureTextPaper, PictureTextPaperComment
from study.models import VideoInfoLectureBanners
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def picture_text_paper(request, pk):
    abs = VideoInfoLectureBanners.objects.all()
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/paper.html', {'paper': papers[0], 'abs': abs, 'comments': comments})
    return HttpResponse('error')


def picture_text_column(request, pk):
    '报名区'
    columns = PictureTextColumn.objects.filter(category='报名区').order_by('id')  # 返回前2条数据
    fs = PictureTextColumn.objects.filter(pk=pk)
    papers = PictureTextPaper.objects.filter(column__pk=pk)
    column = {}
    if len(fs) > 0:
        column = fs[0]

    abs = VideoInfoLectureBanners.objects.all()

    return render(request, 'PictureText/column.html', {'columns': columns,
                                                       'column': column,
                                                       'abs': abs,
                                                       'papers': papers})


def picture_text_category(request, pk):
    '新增栏目：扶阳显议、医案辨析、天天乐、扶阳国医馆'
    abs = VideoInfoLectureBanners.objects.all()
    papers = PictureTextPaper.objects.filter(column__pk=pk)
    if any(papers):
        catename = papers.first().column.category
        columns = PictureTextColumn.objects.filter(category=catename).order_by('id')  # 返回类别列表
        column = {}
        fs = PictureTextColumn.objects.filter(pk=pk)
        if len(fs) > 0:
            column = fs[0]

        return render(request, 'PictureText/category.html',
                      {'columns': columns, 'column': column, 'abs': abs, 'papers': papers})
    else:
        return render(request, 'PictureText/category.html', {'abs': abs})


def picture_text_details(request, pk):
    '新增栏目的详情页面'
    abs = VideoInfoLectureBanners.objects.all()
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/details.html', {'paper': papers[0], 'abs': abs, 'comments': comments})
    return HttpResponse('error')


def picture_text_paper_comment(request, pk):
    if request.method == 'POST':
        new_chat = PictureTextPaperComment.objects.create(
            message=request.POST.get('content'),
            ascription=PictureTextPaper.objects.get(pk=pk),
            author=request.user)

        new_chat.save()

    return HttpResponseRedirect(reverse('picture_text_paper', args=(pk,)))
