from abc import ABC, abstractmethod
from AdminSurveys.Domain.Entity.Suervey import Suervey
class SurveyPort:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def list_suerveys(self, user_id):
        pass

    @abstractmethod
    def get_suervey(self, survey_id):
        pass

    @abstractmethod
    def add_suervey(self, survey:Suervey):
        pass

    @abstractmethod
    def update_suervey(self, survey_id):
        pass

    @abstractmethod
    def delete_suervey(self, survey_id):
        pass
