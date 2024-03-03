from AdminSurveys.Domain.Port.AnswerPort import AnswerPort as Port
from AdminSurveys.Application.UseCase.Answer.CreateAnswerUseCase import CreateAnswerUseCase as UseCase
from flask import jsonify


class CreateController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, request):
        return jsonify(self.__use_case.run(request.get_json()))
