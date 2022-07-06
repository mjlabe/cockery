import random
from typing import List

from django.db.models import Max
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from ninja.pagination import paginate

from apps.question.models import Question

from apps.question.crud import QuestionSchema


api = NinjaAPI(title="question", urls_namespace="question")


@api.get("", response=List[QuestionSchema])
@paginate
def list_questions(request):
    return Question.objects.all()


@api.get("/random", response=QuestionSchema)
def get_random_question_answer(request):
    max_id = Question.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    return Question.objects.filter(id__gte=pk).first()


@api.get("/{question_id}", response=QuestionSchema)
def get_question(request, question_id: int):
    return get_object_or_404(Question, id=question_id)
