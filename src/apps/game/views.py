from typing import List

from ninja import Router
from ninja.pagination import paginate

from apps.game.models import Game, GamePlayer

from apps.game.crud import GameSchema
from apps.question.crud import QuestionSchema

from apps.question.views import get_random_question_answer


router = Router()


@router.get("", response=List[GameSchema])
@paginate
def list_games(request):
    return Game.objects.all()


@router.post("", response=GameSchema)
def create_game(request, game_length: int):
    game = Game.objects.create(game_length=game_length)
    return {"id": game.id}


@router.get("/{game_id}", response=GameSchema)
def get_game_question(request, game_id: int):
    return Game.objects.get(id=game_id)


@router.get("/{game_id}/question", response=QuestionSchema)
def get_random_question(request, game_id: int):
    return get_random_question_answer(request)


# @router.get("/{game_id}", response=QuestionSchema)
# def get_game_question(request, game_id: int):
#     game = get_object_or_404(Game, id=game_id)
#     if game.round >= game.game_length:
#         max_score = GamePlayer.objects.aggregate(Max('score'))
#         winners = GamePlayer.objects.filter(score=max_score)
#         return {
#             "status": "game over",
#             "text": "winner",
#             "answer": winners,
#             "alt_answer": ""
#         }
#     elif game.questions_asked.all():
#         max_id = Question.objects.exclude(id__in=game.questions_asked.all()).aggregate(max_id=Max("id"))['max_id']
#         if not max_id:
#             max_score = GamePlayer.objects.aggregate(Max('score'))
#             winners = GamePlayer.objects.filter(score=max_score)
#             return {
#                 "status": "game over",
#                 "text": "winner",
#                 "answer": winners,
#                 "alt_answer": ""
#             }
#         pk = random.randint(1, max_id)
#         print(Question.objects.filter(id__gte=pk).exclude(id__in=game.questions_asked.all()))
#         question = Question.objects.filter(id__gte=pk).exclude(id__in=game.questions_asked.all()).first()
#     else:
#         max_id = Question.objects.all().aggregate(max_id=Max("id"))['max_id']
#         pk = random.randint(1, max_id)
#         print(game.questions_asked.all())
#         question = Question.objects.filter(id__gte=pk).first()
#
#     game.round += 1
#     game.questions_asked.add(question)
#     game.save()
#
#     if question:
#         question.status = "ok"
#         return question
#     return {
#         "status": "game over",
#         "text": "",
#         "answer": "",
#         "alt_answer": ""
#     }
