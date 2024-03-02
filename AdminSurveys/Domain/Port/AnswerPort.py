from abc import ABC, abstractmethod
from AdminSurveys.Domain.Entity.Answer import Answer


class AnswerPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_answer(self, survey_id):
        pass

    @abstractmethod
    def add_answer(self, answer: Answer):
        pass
