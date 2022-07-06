from typing import List

from ninja import Schema

from apps.question.crud import QuestionSchema


class GameSchema(Schema):
    id: int
    questions_asked: List[QuestionSchema] = []
