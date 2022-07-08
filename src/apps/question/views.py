import random
from typing import List

from django.db.models import Max
from django.shortcuts import get_object_or_404
from ninja import Router

from ninja.pagination import paginate

from apps.game.crud import GamePlayerSchema
from apps.game.models import GamePlayer
from apps.question.models import Question

from apps.question.crud import QuestionSchema


question_router = Router()
game_question_router = Router()


@question_router.get("", response=List[QuestionSchema])
@paginate
def list_questions(request):
    return Question.objects.all()


@question_router.get("/random", response=QuestionSchema)
def get_random_question_answer(request):
    max_id = Question.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    return Question.objects.filter(id__gte=pk).first()


@question_router.get("/{question_id}", response=QuestionSchema)
def get_question(request, question_id: int):
    return get_object_or_404(Question, id=question_id)


@game_question_router.post("{game_id}/question/{question_id}", response=GamePlayerSchema)
def save_player_answer(request, game_id: int, question_id: int, player_name: str, player_answer: str):
    game_player, _ = GamePlayer.objects.get_or_create(
        player_name=player_name,
        game_id=game_id,
    )
    question = Question.objects.get(id=question_id)
    if player_answer == question.answer:
        game_player.score += 1
        game_player.save()

    return game_player
