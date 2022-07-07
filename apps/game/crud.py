from typing import List

from ninja import Schema

from apps.question.crud import QuestionSchema


class GameSchema(Schema):
    id: int
    questions_asked: List[QuestionSchema] = []
    round: int = None
    game_length: int = None


class GamePlayerSchema(Schema):
    id: int
    player_name: str
    game_id: int
    score: int = None
