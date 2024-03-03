from AdminSurveys.Domain.Port.SurveyPort import SurveyPort


class GetSurveyUseCase:
    def __init__(self, repository: SurveyPort):
        self.__repository = repository

    def run(self, survey_id: str):
        return self.__repository.get_survey(survey_id)
