from django.contrib import admin
from apps.question.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
