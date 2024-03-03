from AdminSurveys.Domain.Port.SurveyPort import SurveyPort as Port
from AdminSurveys.Application.UseCase.Survey.GetSurveyUseCase import GetSurveyUseCase as UseCase
from flask import jsonify


class GetController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, survey_id:str):
        return jsonify(self.__use_case.run(survey_id))
