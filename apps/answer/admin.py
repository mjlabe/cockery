from django.contrib import admin
from apps.answer.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
