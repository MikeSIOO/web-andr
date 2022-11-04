from django.db import models

# Create your models here.

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'tags': ['black-jack', 'bender'],
        'answers': [
            {
                'id': answer_id,
                'text': f'Text of answer #{answer_id}',
            } for answer_id in range(2)
        ]
    } for question_id in range(3)
]
