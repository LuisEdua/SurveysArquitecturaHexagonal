from AdminSurveys.Domain.Entity.Survey import Survey
from AdminSurveys.Domain.Port.SurveyPort import SurveyPort


class CreateSurveyUseCase:
    def __init__(self, repository: SurveyPort):
        self.__repository = repository

    def run(self, data):
        survey = Survey(data['title'], data['description'], data['user_id'])
        return self.__repository.add_survey(survey)
