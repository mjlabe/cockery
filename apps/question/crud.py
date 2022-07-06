from ninja import Schema


class QuestionSchema(Schema):
    status: str
    text: str
    answer: str
    alt_answer: str
