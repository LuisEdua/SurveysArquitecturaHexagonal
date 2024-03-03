from AdminSurveys.Domain.Entity.User import User
from AdminSurveys.Domain.Port.UserPort import UserPort


class RegisterUserUseCase:
    def __init__(self, repository:UserPort):
        self.__repository = repository

    def run(self, data):
        user = User(data['email'], data['password'], data['username'], data['cellphone'])
        return self.__repository.register(user)
