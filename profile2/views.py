from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Profile2
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.contrib.auth import update_session_auth_hash, get_user_model
# Create your views here.

def profile(request, id): # url.py에서 넘겨준 인자를 username으로 받는다.
    global Profile
    User = get_user_model()
    user = get_object_or_404(User, id=id)
    Profile = Profile.objects.get(user = user)
    # Profile = Profile.filter(Q(id=id))
    # profile = get_object_or_404(get_user_model(), id = 10)
    return render(request, 'main/navbar.html', {'Profile' : Profile})