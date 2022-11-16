from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TagManager(models.Manager):
    def popular(self):
        return self.order_by('-usage_num')[:10]


class ProfileManager(models.Manager):
    def best(self):
        return self.order_by('-rating')[:5]


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by("-date_create")

    def hot(self):
        return self.order_by("-rating")

    def by_tag(self, tag_name):
        return self.filter(tags__name=tag_name)


class AnswerManager(models.Manager):
    def new(self, id):
        q = Question.objects.get(pk=id)
        return self.filter(question=q).order_by("-date_create")

    def hot(self, id):
        q = Question.objects.get(pk=id)
        return self.filter(question=q).order_by("-rating")


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    usage_num = models.PositiveIntegerField(default=0)

    objects = TagManager()

    def __str__(self):
        return '{} {}'.format(self.name, self.usage_num)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.CharField(max_length=30, unique=True)
    # nick_name = models.CharField(max_length=30, unique=True)
    # password = models.CharField(max_length=30)
    # avatar = models.ImageField()
    # date_create = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username


class Question(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    author = models.ForeignKey(Profile, models.SET_NULL, null=True)
    date_create = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    rating = models.IntegerField(default=0)
    answers_count = models.IntegerField(default=0)

    objects = QuestionManager()

    def __str__(self):
        return '{} {}'.format(self.title, self.rating)


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile, models.SET_NULL, null=True)
    date_create = models.DateField(auto_now_add=True)
    correct = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    question = models.ForeignKey(Question, models.CASCADE)

    objects = AnswerManager()

    def __str__(self):
        return '{} {}'.format(self.rating, self.text)
