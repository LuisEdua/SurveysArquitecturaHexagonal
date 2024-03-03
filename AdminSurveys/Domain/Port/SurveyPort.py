from abc import ABC, abstractmethod
from AdminSurveys.Domain.Entity.Survey import Survey


class SurveyPort:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def list_surveys(self, user_id):
        pass

    @abstractmethod
    def get_survey(self, survey_id):
        pass

    @abstractmethod
    def add_survey(self, survey: Survey):
        pass

    @abstractmethod
    def update_survey(self, survey_id, title, description):
        pass

    @abstractmethod
    def delete_survey(self, survey_id):
        pass
