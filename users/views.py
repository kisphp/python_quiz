from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def user_login(request):
    msg = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('homepage'))
            else:
                msg.append('Your account is disabled')
        else:
            msg.append('Invalid login details supplied');
    data = {
        'msg': '<br>'.join(msg)
    }
    return render(request, 'login.html', data)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))