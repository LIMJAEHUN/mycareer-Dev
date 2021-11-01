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
<<<<<<< HEAD
    return redirect('main:blog')
=======
    return redirect('main/blog.html')

'''
def mark_detail(request,cart_item = None):

    # def profile(request, username): # url.py에서 넘겨준 인자를 username으로 받는다.
    #     profile = get_object_or_404(get_user_model(), username=username)
    #     return render(request, 'main/profile.html', {'profile':profile})
    # try:
    #     mark = Mark.objects.get(mark_id=_mark_id(request))
    #     mark_item = MarkItem.objects.filter(mark=mark, active=True)
    # except ObjectDoesNotExist:
    #     pass
    return render(request, 'main/blog.html')
# def consult2(request):
#     postlist2= mainconsult.objects.all()
#     blog_list = postlist2.filter(name=request.user.username) # 내가 쓴글만
#         # blog_list = Blog.objects.all().order_by('-id') # 블로그 객체 다 가져오기
#     return render(request, 'main/consult_board.html',{'blog_list':blog_list})
def mark(request):
    favor_list = MarkItem.objects.all()
    marklist = favor_list.filter(mark=request.user.id)
    # mark = request.POST.get('MainPost.postname','')
    # marklist = MarkItem.objects.filter(mark_id=mark_id,  available=True)
    # favor_list = MarkItem.objects.all()
    # favor_list2 = Mark.objects.all()
    # marklist = favor_list.filter(mark_id = favor_list2)
    paginator = Paginator(favor_list, 5)
    page = request.GET.get('page')
    # posts = paginator.get_page(page)

    return render(request, 'main/mark.html',{'marklist':marklist})
'''
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0

def mark(request,mark_items = None):
    try:
        mark = Mark.objects.get(mark_id=_mark_id(request))
        mark_items = MarkItem.objects.filter(mark=mark, active=True)
    except ObjectDoesNotExist:
        pass

    return render(request,'main/mark.html', dict(mark_items = mark_items))

<<<<<<< HEAD

=======
# def mark_remove(request, MainPost_id):
#     mark = Mark.objects.get(mark_id=_mark_id(request))
#     MainPost = get_object_or_404(MainPostModel, id = MainPost_id)
#     mark_item = MarkItem.objects.get(MainPost=MainPost, mark=mark)
#     mark_item.delete()
#     return redirect('mark:mark')
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
def delete(request, MainPost_id):
    mark = Mark.objects.get(mark_id=_mark_id(request))
    MainPost = get_object_or_404(MainPostModel, id = MainPost_id)
    mark_item = MarkItem.objects.get(MainPost=MainPost, mark=mark)
    mark_item.delete()
<<<<<<< HEAD
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
=======
    return redirect('main:blog')
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
