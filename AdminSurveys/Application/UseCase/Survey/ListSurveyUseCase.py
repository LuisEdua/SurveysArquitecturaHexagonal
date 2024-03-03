from AdminSurveys.Domain.Port.SurveyPort import SurveyPort


class ListSurveyUseCase:
    def __init__(self, repository: SurveyPort):
        self.__repository = repository

    def run(self, user_id: str):
        return self.__repository.list_surveys(user_id)
