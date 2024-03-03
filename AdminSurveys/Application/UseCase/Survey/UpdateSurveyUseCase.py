from AdminSurveys.Domain.Port.SurveyPort import SurveyPort


class UpdateSurveyUseCase:
    def __init__(self, repository: SurveyPort):
        self.__repository = repository

    def run(self, data, survey_id: str):
        return self.__repository.update_survey(survey_id, data['title'], data['description'])
