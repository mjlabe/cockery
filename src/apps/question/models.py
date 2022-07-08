from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)
    alt_answer = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.text
