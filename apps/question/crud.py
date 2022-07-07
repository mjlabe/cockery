from ninja import Schema


class QuestionSchema(Schema):
    id: int
    status: str
    text: str
    answer: str
    alt_answer: str
