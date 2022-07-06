from django.db import models
from apps.question.models import Question


class Answer(models.Model):
    text = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
