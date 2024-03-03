from AdminSurveys.Domain.Port.SurveyPort import SurveyPort as Port
from AdminSurveys.Application.UseCase.Survey.UpdateSurveyUseCase import UpdateSurveyUseCase as UseCase
from flask import jsonify


class UpdateController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, request, survey_id):
        return jsonify(self.__use_case.run(request.get_json(), survey_id))
