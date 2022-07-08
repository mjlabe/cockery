from django.db import models

from apps.game.models import Game, GamePlayer
from apps.question.models import Question


class Crock(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(GamePlayer, on_delete=models.CASCADE)
    questions_asked = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=20)
