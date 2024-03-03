from AdminSurveys.Domain.Port.SurveyPort import SurveyPort as Port
from AdminSurveys.Application.UseCase.Survey.ListSurveyUseCase import ListSurveyUseCase as UseCase
from flask import jsonify


class ListController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, user_id: str):
        return jsonify(self.__use_case.run(user_id))
