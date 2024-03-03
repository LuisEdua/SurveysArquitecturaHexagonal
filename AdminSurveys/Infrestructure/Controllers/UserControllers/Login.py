from AdminSurveys.Application.UseCase.User.LoginUserUseCase import LoginUserUseCase as UseCase
from AdminSurveys.Domain.Port.UserPort import UserPort as Port
from flask import jsonify


class LoginController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, request):
        return jsonify(self.__use_case.run(request.get_json()))
