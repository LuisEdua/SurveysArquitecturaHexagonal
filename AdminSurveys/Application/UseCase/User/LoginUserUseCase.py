from AdminSurveys.Domain.Port.UserPort import UserPort


class LoginUserUseCase:
    def __init__(self, repository: UserPort):
        self.__repository = repository

    def run(self, data):
        return self.__repository.login(data['email'], data['password'])
