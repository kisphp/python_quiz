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
    url = reverse('question', args=(1,))
    return redirect(url)

def question(request, id):
    if request.method == 'POST':

        print request.session

        if "answer" not in request.session:
            request.session['answer'] = []
        print request.POST.get('answer['+id+']', '-')
        request.session['answer'][int(id)] = int(request.POST.get('answer['+id+']', 0))
        #return redirect(reverse('question', args=((id + 1),)))
    que = Questions.objects.get(pk=int(id))
    data = {
        'q': que,
    }
    return render(request, 'questions/test.html', data)