from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Tag, Question, Answer
from random import choice, sample
from faker import Faker

f = Faker()


class Command(BaseCommand):
    help = 'Fill database with faker data'

    def add_arguments(self, parser):
        parser.add_argument('--profile', '-p', type=int)
        parser.add_argument('--tag', '-t', type=int)
        parser.add_argument('--question', '-q', type=int)
        parser.add_argument('--answer', '-a', type=int)
        parser.add_argument('--ratio', '-r', type=int)

    def fill_profiles(self, count):
        for i in range(count):
            u = User.objects.create_user(f'{f.name()}{f.random_int(min=0, max=1000)}', f.email(), f.password())
            u.save()

            Profile.objects.create(
                rating=f.random_int(min=-100, max=100),
                user=u
            )

    def fill_tags(self, count):
        for i in range(count):
            Tag.objects.create(
                name=f'{f.word()}{f.random_int(min=0, max=10000)}',
                usage_num=f.random_int(min=0, max=1000)
            )

    def fill_questions(self, count):
        profiles_id = list(Profile.objects.values_list('id', flat=True))
        tags_id = list(Tag.objects.values_list('id', flat=True))

        for _ in range(count):
            q = Question.objects.create(
                title='. '.join(f.sentences(f.random_int(min=2, max=3))),
                text='. '.join(f.sentences(f.random_int(min=20, max=40))),
                author=Profile.objects.get(pk=choice(profiles_id)),
                rating=f.random_int(min=0, max=len(profiles_id) - 1),
                answers_count=0,
            )
            q.save()

            cur_tags_id = sample(tags_id, f.random_int(min=1, max=5))
            for tag_id in cur_tags_id:
                q.tags.add(Tag.objects.get(pk=tag_id))

    def fill_answers(self, count):
        profiles_id = list(Profile.objects.values_list('id', flat=True))
        qeustions_id = list(Question.objects.values_list('id', flat=True))

        for _ in range(count):
            q = Question.objects.get(pk=choice(qeustions_id))
            q.answers_count += 1
            q.save()

            a = Answer.objects.create(
                text='. '.join(f.sentences(f.random_int(min=20, max=40))),
                author=Profile.objects.get(pk=choice(profiles_id)),
                correct=choice([True, False]),
                rating=f.random_int(min=0, max=len(profiles_id) - 1),
                question=q,
            )
            a.save()


    def handle(self, *args, **options):
        if (options['profile']):
            self.fill_profiles(options.get('profile', 0))
        if (options['tag']):
            self.fill_tags(options.get('tag', 0))
        if (options['question']):
            self.fill_questions(options.get('question', 0))
        if (options['answer']):
            self.fill_answers(options.get('answer', 0))
        if (options['ratio']):
            ratio = options.get('ratio', 0)
            self.fill_profiles(ratio)
            self.fill_tags(ratio)
            self.fill_questions(ratio * 10)
            self.fill_answers(ratio * 100)
