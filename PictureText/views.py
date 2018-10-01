from django.http import HttpResponse
from django.shortcuts import render
from .models import PictureTextColumn, PictureTextPaper, PictureTextPaperComment
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def picture_text_paper(request, pk):
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/paper.html', {'paper': papers[0], 'comments': comments})
    return HttpResponse('error')

def picture_text_paper1(request, pk):
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/paper.html', {'paper': papers[0], 'comments': comments})
    return HttpResponse('error')

def picture_text_paper2(request, pk):
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/paper.html', {'paper': papers[0], 'comments': comments})
    return HttpResponse('error')

def picture_text_paper3(request, pk):
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/paper.html', {'paper': papers[0], 'comments': comments})
    return HttpResponse('error')

def picture_text_paper4(request, pk):
    papers = PictureTextPaper.objects.filter(pk=pk)

    if len(papers) > 0:
        papers[0].views_count = papers[0].views_count + 1
        papers[0].save()
        comments = PictureTextPaperComment.objects.filter(ascription=papers[0])
        return render(request, 'PictureText/paper.html', {'paper': papers[0], 'comments': comments})
    return HttpResponse('error')


def picture_text_column(request, pk):
    columns = PictureTextColumn.objects.all()
    fs = PictureTextColumn.objects.filter(pk=pk)
    papers = PictureTextPaper.objects.filter(column__pk=pk)
    column = {}
    if len(fs) > 0:
        column = fs[0]

    return render(request, 'PictureText/column.html', {'columns': columns,
                                                       'column': column,
                                                       'papers': papers})

def picture_text_column1(request, pk):
    columns = PictureTextColumn.objects.all()
    fs = PictureTextColumn.objects.filter(pk=pk)
    papers = PictureTextPaper.objects.filter(column__pk=pk)
    column = {}
    if len(fs) > 0:
        column = fs[0]

    return render(request, 'PictureText/column.html', {'columns': columns,
                                                       'column': column,
                                                       'papers': papers})
def picture_text_column2(request, pk):
    columns = PictureTextColumn.objects.all()
    fs = PictureTextColumn.objects.filter(pk=pk)
    papers = PictureTextPaper.objects.filter(column__pk=pk)
    column = {}
    if len(fs) > 0:
        column = fs[0]

    return render(request, 'PictureText/column.html', {'columns': columns,
                                                       'column': column,
                                                       'papers': papers})
def picture_text_column3(request, pk):
    columns = PictureTextColumn.objects.all()
    fs = PictureTextColumn.objects.filter(pk=pk)
    papers = PictureTextPaper.objects.filter(column__pk=pk)
    column = {}
    if len(fs) > 0:
        column = fs[0]

    return render(request, 'PictureText/column.html', {'columns': columns,
                                                       'column': column,
                                                       'papers': papers})
def picture_text_column4(request, pk):
    columns = PictureTextColumn.objects.all()
    fs = PictureTextColumn.objects.filter(pk=pk)
    papers = PictureTextPaper.objects.filter(column__pk=pk)
    column = {}
    if len(fs) > 0:
        column = fs[0]

    return render(request, 'PictureText/column.html', {'columns': columns,
                                                       'column': column,
                                                       'papers': papers})


def picture_text_paper_comment(request, pk):
    if request.method == 'POST':
        new_chat = PictureTextPaperComment.objects.create(
            message=request.POST.get('content'),
            ascription=PictureTextPaper.objects.get(pk=pk),
            author=request.user)

        new_chat.save()

    return HttpResponseRedirect(reverse('picture_text_paper', args=(pk,)))

def picture_text_paper_comment1(request, pk):
    if request.method == 'POST':
        new_chat = PictureTextPaperComment.objects.create(
            message=request.POST.get('content'),
            ascription=PictureTextPaper.objects.get(pk=pk),
            author=request.user)

        new_chat.save()

    return HttpResponseRedirect(reverse('picture_text_paper', args=(pk,)))

def picture_text_paper_comment2(request, pk):
    if request.method == 'POST':
        new_chat = PictureTextPaperComment.objects.create(
            message=request.POST.get('content'),
            ascription=PictureTextPaper.objects.get(pk=pk),
            author=request.user)

        new_chat.save()

    return HttpResponseRedirect(reverse('picture_text_paper', args=(pk,)))

def picture_text_paper_comment3(request, pk):
    if request.method == 'POST':
        new_chat = PictureTextPaperComment.objects.create(
            message=request.POST.get('content'),
            ascription=PictureTextPaper.objects.get(pk=pk),
            author=request.user)

        new_chat.save()

    return HttpResponseRedirect(reverse('picture_text_paper', args=(pk,)))

def picture_text_paper_comment4(request, pk):
    if request.method == 'POST':
        new_chat = PictureTextPaperComment.objects.create(
            message=request.POST.get('content'),
            ascription=PictureTextPaper.objects.get(pk=pk),
            author=request.user)

        new_chat.save()

    return HttpResponseRedirect(reverse('picture_text_paper', args=(pk,)))
