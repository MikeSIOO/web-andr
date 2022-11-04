from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context=context)


def question(request, question_id: int):
    context = {'question': models.QUESTIONS[question_id]}
    return render(request, 'single_question.html', context=context)
