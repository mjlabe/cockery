from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from ninja.pagination import paginate

from apps.question.models import Question
from apps.answer.models import Answer

from apps.question.crud import QuestionSchema, QuestionAnswersSchema


api = NinjaAPI()


@api.get("", response=List[QuestionSchema])
@paginate
def list_questions(request):
    return Question.objects.all()


@api.get("/{question_id}", response=QuestionAnswersSchema)
def get_question(request, question_id: int):
    return get_object_or_404(Question, id=question_id)


@api.get("/random", response=QuestionAnswersSchema)
def get_random_question_answer(request):
    return Question.objects.all()
