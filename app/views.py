import string

from django.core.paginator import Paginator
from django.shortcuts import render
from . import models
from .models import Profile, Tag, Question, Answer


# Create your views here.


def index(request):
    new_questions = Question.objects.new()
    context['questions'] = paginate(new_questions, request)
    context['hot'] = False
    return render(request, 'index.html', context)


def hot(request):
    hot_questions = Question.objects.hot()
    context['questions'] = paginate(hot_questions, request)
    context['hot'] = True
    return render(request, 'index.html', context)


def tag(request, tag_name: string):
    questions_by_tag = Question.objects.by_tag(tag_name)
    context['questions'] = paginate(questions_by_tag, request)
    context['tag_name'] = tag_name
    return render(request, 'tag_search.html', context)


def question(request, question_id: int):
    context['question'] = Question.objects.get(pk=question_id)
    context['answers'] = Answer.objects.hot(question_id)
    return render(request, 'single_question.html', context)


def login(request):
    return render(request, 'log_in.html')


def signup(request):
    return render(request, 'registration.html')


def ask(request):
    return render(request, 'new_question.html')


def settings(request):
    return render(request, 'settings.html')


def paginate(object_list, request):
    # paginator = Paginator(object_list, 3)
    paginator = Paginator(list(object_list), 3)
    page = request.GET.get('page')
    try:
        if int(page) > paginator.num_pages or int(page) < 1:
            objects_page = paginator.get_page(1)
        else:
            objects_page = paginator.get_page(page)
    except:
        objects_page = paginator.get_page(1)
    return objects_page


context = {
    'popular_tags': Tag.objects.popular(),
    'best_members': Profile.objects.best(),
}
