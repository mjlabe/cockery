from typing import List

from ninja import Schema

from apps.answer.crud import AnswerSchema


class QuestionSchema(Schema):
    text: str


class QuestionAnswersSchema(Schema):
    text: str
    answers: List[AnswerSchema]
