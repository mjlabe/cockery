from typing import List

from ninja import Router

from apps.crock.crud import CrockSchema
from apps.crock.models import Crock
from apps.game.models import GamePlayer

router = Router()


@router.post("{game_id}/question/{question_id}/crock", response=CrockSchema)
def save_player_lie(request, game_id: int, question_id: int, player_name: str, player_answer: str):
    game_player, _ = GamePlayer.objects.get_or_create(
        player_name=player_name,
        game_id=game_id,
    )

    return Crock.objects.create(
        game=game_id,
        player=game_player,
        questions_asked=question_id,
        text=player_answer,
    )


@router.get("{game_id}/question/{question_id}/crock", response=List[CrockSchema])
def get_lies(request, game_id: int, question_id: int):
    return Crock.objects.filter(game_id=game_id, questions_asked=question_id)


@router.post("{game_id}/question/{question_id}/crock/answer", response=List[CrockSchema])
def guess_truth(request, game_id: int, question_id: int):
    return Crock.objects.filter(game_id=game_id, questions_asked=question_id)
