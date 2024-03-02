import uuid


class Answer:
    def __init__(self, answer, survey_id, user_id):
        self.uuid = uuid.uuid4()
        self.answer = answer
        self.survey_id = survey_id
        self.user_id = user_id
