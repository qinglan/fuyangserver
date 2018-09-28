from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import VideoCurriculumOrder, VideoInfoStudyFuyangOrder, VideoInfoLectureOrder,Collection


def ordersSortKey(elem):
    return elem.register_date


def userinfo_center(request):
    return render(request, 'userinfo/center.html', {})


def userinfo_collection(request):
    collections = Collection.objects.filter(author=request.user)
    return render(request, 'userinfo/collection.html', {'collections':collections})


def userinfo_center_change(request):
    if request.method == 'POST':
        request.user.country = request.POST.get('profile[title]')
        request.user.province = request.POST.get('profile[signature]')
        request.user.nickname = request.POST.get('profile[truename]')
        request.user.sex = int(request.POST.get('profile[gender]'))
        request.user.real_name = request.POST.get('profile[real_name]')
        request.user.phone_number = request.POST.get('profile[phone_number]')
        request.user.city = request.POST.get('profile[city]')
        request.user.address = request.POST.get('profile[address]')
        request.user.email_address = request.POST.get('profile[email_address]')

        request.user.save()
        return HttpResponseRedirect(reverse('userinfo_center'))
    return HttpResponseRedirect(reverse('userinfo_center'))


def userinfo_orders(request):
    orders = []
    a = VideoCurriculumOrder.objects.filter(purchaser=request.user)
    b = VideoInfoStudyFuyangOrder.objects.filter(purchaser=request.user)
    c = VideoInfoLectureOrder.objects.filter(purchaser=request.user)
    orders.extend(a)
    orders.extend(b)
    orders.extend(c)
    orders.sort(key=ordersSortKey, reverse=True)
    return render(request, 'userinfo/orders.html', {'orders': orders})


def userinfo_invoice(request):
    orders = []
    a = VideoCurriculumOrder.objects.filter(purchaser=request.user,apply_bill=True)
    b = VideoInfoStudyFuyangOrder.objects.filter(purchaser=request.user,apply_bill=True)
    c = VideoInfoLectureOrder.objects.filter(purchaser=request.user,apply_bill=True)
    orders.extend(a)
    orders.extend(b)
    orders.extend(c)
    orders.sort(key=ordersSortKey, reverse=True)
    return render(request, 'userinfo/invoice.html', {'orders': orders})

def userinfo_invoice_cannel(request):
    if 'pk' in request.GET:
        pk = int(request.GET['pk'])
        order = get_order(pk)
        order.apply_bill = False
        order.save()
    return HttpResponse("1")


def userinfo_orders_inner(request):
    if 'pk' in request.GET:
        pk = int(request.GET['pk'])
        order = get_order(pk)
        if order is not None:
            return render(request, 'userinfo/orders_inner.html', {'order': order})
    return HttpResponse("")

def userinfo_orders_invoice(request,pk):

    if request.method == 'POST':
        headName = request.POST.get('headName')
        headType = request.POST.get('headType')
        invoiceSn = request.POST.get('invoiceSn')
        targetEmail = request.POST.get('targetEmail')

        order = get_order(pk)

        if order is not None:
            order.taitou_type = headType
            order.taitou_text = headName
            order.recognition_id = invoiceSn
            order.email = targetEmail
            order.apply_bill = True
            order.save()
            return HttpResponseRedirect(reverse('userinfo_orders'))

    return HttpResponseRedirect(reverse('userinfo_orders'))


def get_order(pk):
    orders = VideoCurriculumOrder.objects.filter(pk=pk)
    if len(orders) > 0:
        return orders[0]

    orders = VideoInfoStudyFuyangOrder.objects.filter(pk=pk)
    if len(orders) > 0:
        return orders[0]

    orders = VideoInfoLectureOrder.objects.filter(pk=pk)
    if len(orders) > 0:
        return orders[0]

    return None