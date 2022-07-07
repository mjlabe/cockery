import random
from typing import List

from django.db.models import Max
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from ninja.pagination import paginate

from apps.question.models import Question
from apps.game.models import Game, GamePlayer

from apps.question.crud import QuestionSchema
from apps.game.crud import GameSchema, GamePlayerSchema

api = NinjaAPI(title="game", urls_namespace="game")


@api.get("", response=List[GameSchema])
@paginate
def list_games(request):
    return Game.objects.all()


@api.post("", response=GameSchema)
def create_game(request, game_length: int):
    game = Game.objects.create(game_length=game_length)
    return {"id": game.id}


@api.get("{game_id}", response=QuestionSchema)
def get_game_question(request, game_id: int):
    game = get_object_or_404(Game, id=game_id)
    if game.round >= game.game_length:
        max_score = GamePlayer.objects.aggregate(Max('score'))
        winners = GamePlayer.objects.filter(score=max_score)
        return {
            "status": "game over",
            "text": "winner",
            "answer": winners,
            "alt_answer": ""
        }
    elif game.questions_asked.all():
        max_id = Question.objects.exclude(id__in=game.questions_asked.all()).aggregate(max_id=Max("id"))['max_id']
        if not max_id:
            max_score = GamePlayer.objects.aggregate(Max('score'))
            winners = GamePlayer.objects.filter(score=max_score)
            return {
                "status": "game over",
                "text": "winner",
                "answer": winners,
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

    game.round += 1
    game.questions_asked.add(question)
    game.save()

    if question:
        question.status = "ok"
        return question
    return {
        "status": "game over",
        "text": "",
        "answer": "",
        "alt_answer": ""
    }


@api.post("{game_id}/{question_id}", response=GamePlayerSchema)
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
