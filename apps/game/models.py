from django.db import models

from apps.question.models import Question


class Game(models.Model):
    questions_asked = models.ManyToManyField(Question)


class PlayerAnswer(models.Model):
    player_name = models.CharField(max_length=20)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50)
