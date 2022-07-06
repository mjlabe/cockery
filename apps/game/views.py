import random
from typing import List

from django.db.models import Max
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from ninja.pagination import paginate

from apps.question.models import Question
from apps.game.models import Game

from apps.question.crud import QuestionSchema
from apps.game.crud import GameSchema

api = NinjaAPI(title="game", urls_namespace="game")


@api.get("", response=List[GameSchema])
@paginate
def list_games(request):
    return Game.objects.all()


@api.post("", response=GameSchema)
def create_game(request):
    game = Game.objects.create()
    return {"id": game.id}


@api.get("{game_id}/random", response=QuestionSchema)
def get_random_game_question_answer(request, game_id: int):
    game = get_object_or_404(Game, id=game_id)
    if game.questions_asked.all():
        max_id = Question.objects.exclude(id__in=game.questions_asked.all()).aggregate(max_id=Max("id"))['max_id']
        if not max_id:
            return {
                "status": "game over",
                "text": "",
                "answer": "",
                "alt_answer": ""
            }
        pk = random.randint(1, max_id)
        print(Question.objects.filter(id__gte=pk).exclude(id__in=game.questions_asked.all()))
        question = Question.objects.filter(id__gte=pk).exclude(id__in=game.questions_asked.all()).first()
    else:
        max_id = Question.objects.all().aggregate(max_id=Max("id"))['max_id']
        pk = random.randint(1, max_id)
        print(game.questions_asked.all())
        question = Question.objects.filter(id__gte=pk).first()

    game.questions_asked.add(question)

    if question:
        question.status = "ok"
        return question
    return {
        "status": "game over",
        "text": "",
        "answer": "",
        "alt_answer": ""
    }
