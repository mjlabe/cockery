from ninja import Schema


class AnswerSchema(Schema):
    text: str
    question_id: int
