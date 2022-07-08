from django.db import models

from apps.question.models import Question


class Game(models.Model):
    questions_asked = models.ManyToManyField(Question)
    round = models.IntegerField(default=0)
    game_length = models.IntegerField(default=10)


class GamePlayer(models.Model):
    player_name = models.CharField(max_length=20)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
