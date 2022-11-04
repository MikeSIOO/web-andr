import string

from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    context = {'questions': models.QUESTIONS, 'hot': False}
    return render(request, 'index.html', context=context)


def hot(request):
    context = {'questions': models.QUESTIONS, 'hot': True}
    return render(request, 'index.html', context=context)


def tag(request, tag_name: string):
    context = {'questions': models.QUESTIONS, 'tag_name': tag_name}
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
