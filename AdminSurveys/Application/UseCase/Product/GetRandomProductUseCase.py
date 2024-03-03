from AdminSurveys.Domain.Port.ProductPort import ProductPort


class GetRandomProductUseCase:
    def __init__(self, repository: ProductPort):
        self.__repository = repository

    def run(self, survey_id):
        return self.__repository.get_random_product(survey_id)
