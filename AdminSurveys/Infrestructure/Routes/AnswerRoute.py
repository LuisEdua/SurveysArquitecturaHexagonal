from AdminSurveys.Infrestructure.Controllers.AnswerControllers.Create import CreateController
from AdminSurveys.Infrestructure.Controllers.AnswerControllers.Get import GetController
from AdminSurveys.Infrestructure.Repository.MySQLAnswerRepository import MySQLAnswerRepository
from flask import Blueprint, request

repository = MySQLAnswerRepository()
create_controller = CreateController(repository)
get_controller = GetController(repository)

answer_routes = Blueprint('answer_routes', __name__)


@answer_routes.route('/<string:question_id>', methods=['GET'])
def get_answers(question_id):
    return get_controller.run(question_id)


@answer_routes.route('/', methods=['POST'])
def create_answer():
    return create_controller.run(request)
