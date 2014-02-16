import random
from django.shortcuts import render, HttpResponse, redirect
from questions.models import *
from django.core.urlresolvers import reverse

def homepage(request):
    questions = Questions.objects.all()
    try:
        ses = request.session['page']
    except KeyError:
        ses = '-not set-'
    data = {
        'questions': questions,
        'session': ses
    }
    return render(request, 'questions/homepage.html', data)

def startquiz(request):
    questions = Questions.objects.values_list('id', flat=True).all()
    que = []
    while (len(que) < 3):
        ran = random.choice(questions)
        if ran not in que:
            que.append(ran)
    request.session['question'] = que
    return redirect(reverse('homepage'))