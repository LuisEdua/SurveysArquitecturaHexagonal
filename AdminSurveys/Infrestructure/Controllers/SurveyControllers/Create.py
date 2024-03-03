from AdminSurveys.Domain.Port.SurveyPort import SurveyPort as Port
from AdminSurveys.Application.UseCase.Survey.CreateSurveyUseCase import CreateSurveyUseCase as UseCase
from flask import jsonify


class CreateController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, request):
        return jsonify(self.__use_case.run(request.get_json()))
