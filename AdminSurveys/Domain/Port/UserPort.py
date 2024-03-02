from abc import ABC, abstractmethod
from AdminSurveys.Domain.Entity.User import User


class UserPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def login(self, email, password):
        pass

    @abstractmethod
    def register(self, user:User):
        pass
