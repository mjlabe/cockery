from ninja import Schema

from apps.game.crud import GameSchema, GamePlayerSchema
from apps.question.crud import QuestionSchema


class CrockSchema(Schema):
    id: int
    game: GameSchema
    player: GamePlayerSchema
    questions_asked: QuestionSchema
    text: str
