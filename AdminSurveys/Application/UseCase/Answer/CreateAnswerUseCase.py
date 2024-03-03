from AdminSurveys.Domain.Entity.Answer import Answer
from AdminSurveys.Domain.Port.AnswerPort import AnswerPort


class CreateAnswerUseCase:
    def __init__(self, repository: AnswerPort):
        self.__repository = repository

    def run(self, data):
        answer = Answer(data['answer'], data['questionid'], data['userid'])
        return self.__repository.add_answer(answer)
