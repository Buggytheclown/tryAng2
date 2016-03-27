from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import viewsets

from Polls.models import Question, Choice
from Polls.serializers import PollsSerializer


class PollsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = PollsSerializer


def PollsVoteUp(request, *args, **kwargs):
    question_id = kwargs['question_id']
    choice_id = kwargs['choice_id']
    msg = 'BIG_fail'
    try:
        question = Question.objects.get(id=question_id)
        choice = question.choices.get(id=choice_id)
        msg = choice.vote_up()
    except ObjectDoesNotExist:
        msg = 'fail'
    return JsonResponse({'detail': msg})
