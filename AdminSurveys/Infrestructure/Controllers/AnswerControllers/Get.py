from AdminSurveys.Domain.Port.AnswerPort import AnswerPort as Port
from AdminSurveys.Application.UseCase.Answer.GetAnswersUseCase import GetAnswersUseCase as UseCase
from flask import jsonify


class GetController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, question_id: str):
        return jsonify(self.__use_case.run(question_id))
