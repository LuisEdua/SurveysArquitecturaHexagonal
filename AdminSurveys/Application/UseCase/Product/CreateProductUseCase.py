from AdminSurveys.Domain.Port.ProductPort import ProductPort
from AdminSurveys.Domain.Entity.Product import Product


class CreateProductUseCase:
    def __init__(self, repository: ProductPort):
        self.__repository = repository

    def create_product(self, data):
        product = Product(data['name'], data['survey_id'], data['description'])
        return self.__repository.create_product(product)
