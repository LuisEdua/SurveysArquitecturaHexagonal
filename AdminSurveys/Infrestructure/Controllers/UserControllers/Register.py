from AdminSurveys.Domain.Port.UserPort import UserPort as Port
from AdminSurveys.Application.UseCase.User.RegisterUserUseCase import RegisterUserUseCase as UseCase
from flask import jsonify


class RegisterController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, request):
        return jsonify(self.__use_case.run(request.get_json()))
