from AdminSurveys.Infrestructure.Controllers.SurveyControllers.Delete import DeleteController
from AdminSurveys.Infrestructure.Controllers.SurveyControllers.Get import GetController
from AdminSurveys.Infrestructure.Controllers.SurveyControllers.List import ListController
from AdminSurveys.Infrestructure.Controllers.SurveyControllers.Update import UpdateController
from AdminSurveys.Infrestructure.Repository.MySQLSurveyRepository import MySQLSurveyRepository
from AdminSurveys.Infrestructure.Controllers.SurveyControllers.Create import CreateController
from flask import Blueprint, request

repository = MySQLSurveyRepository()
create_controller = CreateController(repository)
get_controller = GetController(repository)
list_controller = ListController(repository)
update_controller = UpdateController(repository)
delete_controller = DeleteController(repository)

survey_routes = Blueprint('survey_routes', __name__)


@survey_routes.route('/list/<string:user_id>', methods=['GET'])
def get_surveys(user_id):
    return list_controller.run(user_id)


@survey_routes.route('/<string:survey_id>', methods=['GET'])
def get_survey(survey_id):
    return get_controller.run(survey_id)


@survey_routes.route('/', methods=['POST'])
def create_survey():
    return create_controller.run(request)


@survey_routes.route('/<string:survey_id>', methods = ['PUT'])
def update_survey(survey_id):
    return update_controller.run(request, survey_id)


@survey_routes.route('/<string:survey_id>', methods = ['DELETE'])
def delete_survey(survey_id):
    return delete_controller.run(survey_id)
