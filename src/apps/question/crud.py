from ninja import Schema


class QuestionSchema(Schema):
    id: int
    text: str
    answer: str
    alt_answer: str = None
