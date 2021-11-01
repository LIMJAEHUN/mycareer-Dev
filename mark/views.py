from django.shortcuts import  get_object_or_404,render, redirect
from main.models import MainPost as MainPostModel
from.models import Mark, MarkItem
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user, get_user_model, login as dj_login

def _mark_id(request):
    mark = request.user.id
    # mark = request.session.session_key
    # if not mark:
    #     mark = request.session.create()
    return mark

def add_mark(request, MainPost_id):
    global MainPost
    # MainPost = MainPost.objects.get(id = MainPost_id)
    MainPost = get_object_or_404(MainPostModel, id = MainPost_id)

    try:
        mark = Mark.objects.get(mark_id=_mark_id(request))
    except Mark.DoesNotExist:
        mark = Mark.objects.create(
            mark_id = _mark_id(request)
        )
        mark.save()

    try:
        mark_item = MarkItem.objects.get(MainPost=MainPost, mark=mark)
        mark_item.quantity += 1
        mark_item.save()
    except MarkItem.DoesNotExist:
        mark_item = MarkItem.objects.create(
            MainPost = MainPost,
            quantity = 1,
            mark= mark
        )
        mark_item.save()
    return redirect('main:blog')

def mark(request,mark_items = None):
    try:
        mark = Mark.objects.get(mark_id=_mark_id(request))
        mark_items = MarkItem.objects.filter(mark=mark, active=True)
    except ObjectDoesNotExist:
        pass

    return render(request,'main/mark.html', dict(mark_items = mark_items))


def delete(request, MainPost_id):
    mark = Mark.objects.get(mark_id=_mark_id(request))
    MainPost = get_object_or_404(MainPostModel, id = MainPost_id)
    mark_item = MarkItem.objects.get(MainPost=MainPost, mark=mark)
    mark_item.delete()
    return redirect('main:blog')

# def mark(request,mark_items = None):
#     try:
#         mark = Mark.objects.get(mark_id=_mark_id(request))
#         mark_items = MarkItem.objects.filter(mark=mark, active=True)
#     except ObjectDoesNotExist:
#         pass
#     # mark = request.POST.get('MainPost.postname','')
#     # marklist = MarkItem.objects.filter(mark_id=mark_id,  available=True)
#     # favor_list = MarkItem.objects.all()
#     # favor_list2 = Mark.objects.all()
#     # marklist = favor_list.filter(mark_id = favor_list2)
#
#     # posts = paginator.get_page(page)
#
#     return render(request, 'main/blog.html',dict(mark_items = mark_items))
