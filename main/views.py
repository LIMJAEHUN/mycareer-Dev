#from typing_extensions import Required
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.urls import  reverse
from django.contrib.auth import authenticate, get_user, get_user_model, login as dj_login
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
<<<<<<< HEAD
from .models import member, MainPost, chosunPost,mainconsult,seoulconsult,chosunconsult,Profile
=======
from .models import member, MainPost, chosunPost,mainconsult,seoulconsult,chosunconsult#,Profile
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum
from django.views.generic import ListView
from main.forms import UserForm
from .forms import consult_form ,ProfileForm,CustomUserChangeForm
import os
from mysetting import SECRET_KEY,KAKAO_KEY
from django.views import View
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from allauth.socialaccount.providers.kakao import views as kakao_view
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.contrib import messages
<<<<<<< HEAD
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from mark.models import Mark, MarkItem
from django.core.exceptions import ObjectDoesNotExist

def nopage(request):
    return render(request,'main/nopage.html', {'success':success})
=======
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from mark.models import Mark, MarkItem

def navbar(request, id):
    profile = get_object_or_404(get_user_model(), id=id)
    return render(request, 'main/base.html', {'profile':profile})
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0

def signup2(request):
    return render(request,'main/signup2.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            university = form.cleaned_data.get('university')
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
            return redirect('main:blog')

    else:
        form = UserForm()
    return render(request, 'main/signup.html', {'form': form})

<<<<<<< HEAD

def profile(request, id): # url.py?????? ????????? ????????? username?????? ?????????.
    global Profile

    User = get_user_model()
    user = get_object_or_404(User, id=id)
    Profile = Profile.objects.get(user = user)
    # Profile = Profile.filter(Q(id=id))
    # profile = get_object_or_404(get_user_model(), id = 10)
    return render(request, 'main/navbar.html', {'Profile' : Profile})


=======
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
def search(request):
    posts = MainPost.objects.all().order_by('-id')
    atags = request.POST.getlist('atags','')
    jtags = request.POST.getlist('jtags','')
    etags = request.POST.getlist('etags','')
    kw = request.POST.get('kw')

    q = Q()
    if jtags:
        q.add(Q(job__in=jtags), q.AND)
    if atags:
        q.add(Q(area__in=atags), q.AND)
    if etags:
        q.add(Q(etc__in=etags), q.AND)

    posts = MainPost.objects.filter(q).distinct()





    if kw:
        posts = MainPost.objects.filter(Q(postname=kw)|Q(author=kw)|Q(job=kw)|Q(area=kw))
        if atags:
            q.add(Q(area__in=atags), q.AND)
            posts = MainPost.objects.filter(Q(area__istartswith=atags)&Q(postname=kw)|Q(author=kw)|Q(job=kw)|Q(area=kw))
            return render(request, 'main/search.html', {'posts' : posts, 'tags' : tags})
        return render(request, 'main/search.html', {'posts': posts, 'kw': kw})
    else:
        return render(request, 'main/search.html', {'posts' : posts})



    # if kw is not None and tag is not None:
    #posts = Post.objects.filter((Q(jop__in=tags)&Q(area__in=tags))&Q(etc__in=tags))
    #     q.add (Q(jop__in=tags),Q.)
    #     posts = posts.filter(Q(postname=kw)|Q(author=kw)|Q(jop=kw))
    #
    # return render(request, 'main/search.html', {'posts' : posts})
    #


# def tags(request):
#     jop = request.POST.get('',None)
#     jop_count  = Post.objects.filter(jop).aggregate(sum('jop'))
#     pots.stories_filed += 1
#     posts.save()
#
#     return render(request, 'main/blog.html',{'jop_count': jop_count})
#
#
def success(request):
    return render(request,'main/success.html', {'success':success})

<<<<<<< HEAD
=======
def nopage(request):
    return render(request,'main/nopage.html', {'success':success})

>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
def index(request):
    return render(request,'main/index.html')

def login(request):
    return render(request,'main/login.html')


# def blog(request):
#     return render(request, 'main/blog.html')
<<<<<<< HEAD
def _mark_id(request):
    mark = request.user.id
    # mark = request.session.session_key
    # if not mark:
    #     mark = request.session.create()
    return mark

=======
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
def blog(request):
    global MarkItem
    mark = request.user.id
    postlist  = MainPost.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    pagenator = Paginator(postlist, 10)
    postlist  = pagenator.get_page(page)
    mark_items = MarkItem.objects.all()
    mark_items = MarkItem.objects.filter(mark=mark, active=True)
<<<<<<< HEAD

    return render(request, 'main/blog.html', {'postlist':postlist,'mark_items':mark_items})

    postlist  = MainPost.objects.all().order_by('-id')

    search_key = request.GET.get('search_key')
    if search_key: # ?????? ???????????? ????????????
        post_list = post_list.filter(wtite__icontains=search_key) # ?????? ???????????? ????????? queryset ????????????

    return render(request, 'main/blog.html', {'blog':blog})

=======
    
    return render(request, 'main/blog.html', {'postlist':postlist,'mark_items':mark_items})

>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
def posting(request, pk):
    Mainpost = {'Mainpost': MainPost.objects.all()}
    Mainpost = MainPost.objects.get(pk=pk)
    return render(request, 'main/posting.html',{'Mainpost':Mainpost})


def remove_post(request, pk):
    post = MainPost.objects.get(pk=pk)
    if request.method == 'POST':
        Mainpost.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})


# def consult(request):
#     return render(request,'main/consult.html')

<<<<<<< HEAD
# def profile(request, id): # url.py?????? ????????? ????????? username?????? ?????????.
#     global Profile
#     # Profile = {'Profile': Profile.objects.all()}
#     Profile = Profile.objects.filter(id = 10)
#     # profile = get_object_or_404(get_user_model(), id = 10)
#     return render(request, 'main/profile.html', dict(Profile = Profile))
# mark = Mark.objects.get(mark_id=_mark_id(request))
# mark_items = MarkItem.objects.filter(mark=mark, active=True)

def change_profile(request, username):
=======
# def profile(request, username): # url.py?????? ????????? ????????? username?????? ?????????.
#     profile = get_object_or_404(get_user_model(), username=username)
#     return render(request, 'main/profile.html', {'profile':profile})

# def profile(request, id): # url.py?????? ????????? ????????? username?????? ?????????.
#    profile = get_object_or_404(get_user_model(), id=id)
#    return render(request, 'main/base.html', {'profile':profile})


def change_profile(request, id):
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()
            profile_form.save()
<<<<<<< HEAD
            return redirect('main:profile',user.username)
=======
            return redirect('main:profile',user.id)
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
        return redirect('main:change_profile')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        # ????????? ???????????? ?????? ????????? ???????????? ????????? ?????????
        # ????????? ????????? ???????????? ?????? instance??? ???????????? ??????.
        profile, create = Profile.objects.get_or_create(user=request.user)
        # Profile ????????? User ????????? 1:1 ????????? ???????????????
        # User ????????? ????????? ??????????????? ??????????????? ?????? ?????? ???????????? Profile ??????????????? ???????????? ?????? ????????? ?????????
        # ???????????? Profile ??????????????? ????????? ????????? ????????????, ????????? ?????? ??????????????? ??????.
        profile_form = ProfileForm(instance=profile)
        return render(request, 'main/change_profile.html', {
                'user_change_form': user_change_form,
                'profile_form': profile_form
        })

'''
@login_required
def change_password(request, username):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '???????????? ????????? ?????????????????????.')
            return redirect('main:profile',user.username)
        else:
            messages.error(request, '????????? ??????????????????. ?????? ??????????????????.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/change_password.html'), {'form':form}
'''

'''
def Consult(request, point_id):
    form = consult_form(request.POST)
    if request.method == "POST" and form.is_valid():
            form = mainconsult()
            form.consult_id = request.POST['id']
            form.name = request.POST['name']
            form.phone_number = request.POST['phone_number']
            form.university = request.POST['university']
            form.postname = request.POST['postname']
            form.contents = request.POST['contents']
            form.save()
            return redirect('/blog/')
    else:
        form = consult_form()
    return render(request, 'main/Consult.html', {'form': form})
'''

'''
def point(request, pid):
    point_detail = get_object_or_404(point, pk=pid)
    return render(request, 'main/consult.html',{'point':point_detail})
'''


'''?????? ?????????
def Consult(request,point_id):
    form = consult_form(request.POST)
    # post = MainPost.objects.all(point_id)
    if request.method == "POST" and form.is_valid() :
<<<<<<< HEAD

=======
        
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
        if point_id == "2":
            form = seoulconsult()
            form.name = request.POST['name']
            form.phone_number = request.POST['phone_number']
            form.university = request.POST['university']
            form.contents = request.POST['contents']
            form.save()
            return redirect('main:blog')

        if point_id == "1":
            form = chosunconsult()
            form.name = request.POST['name']
            form.phone_number = request.POST['phone_number']
            form.university = request.POST['university']
            form.contents = request.POST['contents']
            form.save()

            return redirect('main:blog')

    else:
        form = consult_form()
    return render(request, 'main/Consult.html', {'form': form})#,{'consult':consult})
'''

def Consult(request,point_id):
    if request.method == "POST":
        form = consult_form(request.POST)
        if form.is_valid() :
            form = mainconsult()
            form.username = request.POST['username']
            form.name = request.POST['name']
            form.phone_number = request.POST['phone_number']
            form.university = request.POST['university']
            #form.university = form.cleaned_data.get('university')
            form.contents = request.POST['contents']
            form.save()
<<<<<<< HEAD
            return redirect('/success')
=======
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
        if point_id == "2":
            form = seoulconsult()
            form.username = request.POST['username']
            form.name = request.POST['name']
            form.phone_number = request.POST['phone_number']
            form.university = request.POST['university']
            form.contents = request.POST['contents']
            form.save()
            return redirect('/success')
        if point_id == "1":
            form = chosunconsult()
            form.username = request.POST['username']
            form.name = request.POST['name']
            form.phone_number = request.POST['phone_number']
            form.university = request.POST['university']
            form.contents = request.POST['contents']
            form.save()
            return redirect('/success')

    else:
        form = consult_form()
    #return render(request, 'main/blog/<int:pk>.html', {'form': form})#,{'consult':consult})
    return render(request, 'main/Consult.html', {'form': form})#,{'consult':consult})
    #return render(request, 'main/posting.html', {'form': form})#,{'consult':consult})

#?????? ??? ?????? ????????? ?????? ???????????? ??????????????????
def consult2(request):
    postlist2= mainconsult.objects.all().order_by('-id')
<<<<<<< HEAD
    blog_list = postlist2.filter(username=request.user.username)
=======
    blog_list = postlist2.filter(username=request.user.username) 
    #postlist2= mainconsult.objects.all().order_by('-id')
    #blog_list = postlist2.filter(name=request.user.username) 
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    return render(request, 'main/consult_board.html',{'blog_list':blog_list})

def consult2_popup(request, pk):
    consult2_detail = mainconsult.objects.get(id=pk)
    return render(request, 'main/consult2_popup.html', {'details':consult2_detail})


'''
def kakao_login(request):
    app_rest_api_key = os.environ.get("f7392204050136e895a59bbdcb9090db")
<<<<<<< HEAD
    redirect_uri = main_domain + "accounts/kakao/login/callback"
=======
    redirect_uri = main_domain + "accounts/kakao/login/callback" 
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={'f7392204050136e895a59bbdcb9090db'}&redirect_uri={'http://127.0.0.1:8000/'}&response_type=code"
    )
'''


class KakaoSignInView(View):
    def get(self, request):
        client_id = KAKAO_KEY['KAKAO_KEY']
        redirect_uri = main_domain + "accounts/kakao/login/callback"
        return redirect(
                f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={'http://127.0.0.1:8000'}&response_type=code"
            )

class KakaoSignInCallbackView(View):
    def get(self, request):
        try:
            code            = request.GET.get("code")
            client_id       = KAKAO_KEY['KAKAO_KEY']
            redirect_uri    = main_domain + "accounts/kakao/login/callback"
            token_request   = requests.get(
                f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={'http://127.0.0.1:8000'}&code={code}"
            )
            token_json      = token_request.json()
            #print(token_json)

            error           = token_json.get("error", None)

            if error is not None:
                return JsonResponse({"message":"INVALD_CODE"}, status=400)

            access_token    = token_json.get("access_token")

            profile_request     = requests.get(
                "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"},
            )

            profile_json        = profile_request.json()
            kakao_account       = profile_json.get("kakao_account")
            email               = kakao_account.get("email", None)
            kakao_id            = profile_json.get("id")
            profileImageUR      = profile_json.get("profile_image")
            nickName            = profile_json.get("nickname")


        except KeyError:
            return JsonResponse({"message":"INVALID_TOKEN"}, status=400)

        except access_token.DoesNotExist:
            return JsonResponse({"message":"INVALID_TOKEN"}, status=400)
        if member.objects.filter(social_account = kakao_id).exists():
            kakao_user    = member.objects.get(social_account = kakao_id)
            token   = jwt.encode({"email":email}, SECRET['SECRET_KEY'], algorithm="HS256")
            token   = token.decode("utf-8")

            print("success")

            return JsonResponse({"token" : token}, status=200)

        else:
            member(social_account = kakao_id,
                email    = email,
            ).save()
            token = jwt.encode({"email" : email}, SECRET['SECRET_KEY'], algorithm = "HS256")
            token = token.decode("utf-8")
<<<<<<< HEAD
            return JsonResponse({"token" : token}, status = 200)
=======
            return JsonResponse({"token" : token}, status = 200)
>>>>>>> 6019f41c016fb3ae71ff4ca90e86f0a78662aec0
