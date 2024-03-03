from AdminSurveys.Domain.Port.SurveyPort import SurveyPort as Port
from AdminSurveys.Application.UseCase.Survey.DeleteSurveyUseCase import DeleteSurveyUseCase as UseCase
from flask import jsonify


class DeleteController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, survey_id):
        return jsonify(self.__use_case.run(survey_id))
