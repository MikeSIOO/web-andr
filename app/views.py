import string

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    # context = {'questions': models.QUESTIONS, 'hot': False}
    context = {'questions': paginate(list(models.QUESTIONS), request), 'hot': False}
    return render(request, 'index.html', context=context)


def hot(request):
    # context = {'questions': models.QUESTIONS, 'hot': True}
    context = {'questions': paginate(list(models.QUESTIONS), request), 'hot': True}
    return render(request, 'index.html', context=context)


def tag(request, tag_name: string):
    # context = {'questions': models.QUESTIONS, 'tag_name': tag_name}
    context = {'questions': paginate(list(models.QUESTIONS), request), 'tag_name': tag_name}
    return render(request, 'tag_search.html', context=context)


def question(request, question_id: int):
    context = {'question': models.QUESTIONS[question_id]}
    return render(request, 'single_question.html', context=context)


def login(request):
    return render(request, 'log_in.html')


def signup(request):
    return render(request, 'registration.html')


def ask(request):
    return render(request, 'new_question.html')


def settings(request):
    return render(request, 'settings.html')


def paginate(object_list, request):
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page
