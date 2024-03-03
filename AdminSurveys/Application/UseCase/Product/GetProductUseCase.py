from AdminSurveys.Domain.Port.ProductPort import ProductPort


class GetProductUseCase:
    def __init__(self, repository: ProductPort):
        self.__repository = repository

    def run(self, product_id):
        return self.__repository.get_product(product_id)
