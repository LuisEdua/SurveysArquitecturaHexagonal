from AdminSurveys.Domain.Port.ProductPort import ProductPort as Port
from AdminSurveys.Application.UseCase.Product.GetRandomProductUseCase import GetRandomProductUseCase as UseCase
from flask import jsonify


class GetRandom:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, survey_id: str):
        return jsonify(self.__use_case.run(survey_id))
