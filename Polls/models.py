from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    timestamp = models.DateTimeField('Was created', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def vote_up(self):
        self.votes += 1
        self.save()
        return 'success'

    def __str__(self):
        return '%s:%s' % (self.choice_text, self.votes)