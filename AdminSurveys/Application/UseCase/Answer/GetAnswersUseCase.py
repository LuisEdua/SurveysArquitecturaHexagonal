from AdminSurveys.Domain.Port.AnswerPort import AnswerPort


class GetAnswersUseCase:
    def __init__(self, repository: AnswerPort):
        self.repository = repository

    def run(self, question_id: str):
        return self.repository.get_answer(question_id)
