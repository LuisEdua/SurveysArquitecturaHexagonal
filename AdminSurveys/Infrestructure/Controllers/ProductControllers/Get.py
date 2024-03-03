from AdminSurveys.Domain.Port.ProductPort import ProductPort as Port
from AdminSurveys.Application.UseCase.Product.GetProductUseCase import GetProductUseCase as UseCase
from flask import jsonify


class GetController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, product_id: str):
        return jsonify(self.__use_case.run(product_id))
