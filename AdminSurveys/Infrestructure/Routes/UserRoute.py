from AdminSurveys.Infrestructure.Controllers.UserControllers.Register import RegisterController
from AdminSurveys.Infrestructure.Repository.MySQLUserRepository import MySQLUserRepository
from AdminSurveys.Infrestructure.Controllers.UserControllers.Login import LoginController
from flask import Blueprint, request

repository = MySQLUserRepository()
login_controller = LoginController(repository)
register_controller = RegisterController(repository)

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/login', methods=['POST'])
def login():
    return login_controller.run(request)


@user_routes.route('/register', methods=['POST'])
def register():
    return register_controller.run(request)
