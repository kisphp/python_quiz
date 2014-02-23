import random
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from questions.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

MAX_QUESTIONS = 3


@login_required(login_url='/login')
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
    all_questions = Questions.objects.values_list('id', flat=True).all()
    que = []
    if 'step' in request.session:
        del(request.session['step'])
    while (len(que) < MAX_QUESTIONS):
        ran = random.choice(all_questions)
        if ran not in que:
            que.append(ran)

    test = Tests.objects.create(user=request.user)
    for q in que:
        qq = Questions.objects.get(pk=q)
        TestsQuestions.objects.create(test=test, question=qq)


    url = reverse('question', args=(test.pk,))
    return redirect(url)

def finish(request):
    return render(request, 'questions/finish.html')



#@login_required(login_url=reverse('homepage'))
def question(request, id):
    if 'step' not in request.session:
        request.session['step'] = 0

    try:
        test = Tests.objects.get(pk=int(id))
    except Tests.DoesNotExist:
        return HttpResponse('acest test nu exista')
    test_questions = TestsQuestions.objects.filter(test=test)

    if request.method == 'POST':
        request.session['step'] += 1
        if request.session['step'] > MAX_QUESTIONS:
            return redirect(reverse('homepage'))

        if int(request.session['step']) >= len(test_questions):
            return redirect(reverse('finish'))

        current_question = test_questions[request.session['step']].question

        for quest in request.POST.getlist('answer'):
            print quest
            answer = Answers.objects.get(pk=int(quest))

            r = Responses()
            r.test = test
            r.question = current_question
            r.answer = answer
            r.save()

        return redirect(reverse('question', args=(id,)))

    if test.started == 0:
        test.started = 1
        test.save()

    print "Step: %s" % request.session['step']


    que = test_questions[request.session['step']]
    data = {
        'q': que.question,
        'step': ( request.session['step'] + 1)
    }
    return render(request, 'questions/test.html', data)