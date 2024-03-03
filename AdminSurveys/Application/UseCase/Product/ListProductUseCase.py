from AdminSurveys.Domain.Port.ProductPort import ProductPort


class ListProductUseCase:
    def __init__(self, repository: ProductPort):
        self.__repository = repository

    def run(self, survey_id: str):
        return self.__repository.list_products(survey_id)
