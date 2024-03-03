from AdminSurveys.Infrestructure.Controllers.ProductControllers.Create import CreateController
from AdminSurveys.Infrestructure.Controllers.ProductControllers.Get import GetController
from AdminSurveys.Infrestructure.Controllers.ProductControllers.GetRandom import GetRandomController
from AdminSurveys.Infrestructure.Controllers.ProductControllers.List import ListController
from AdminSurveys.Infrestructure.Repository.MySQLProductRepository import MySQLProductRepository
from flask import Blueprint, request


repository = MySQLProductRepository()
create_controller = CreateController(repository)
get_controller = GetController(repository)
list_controller = ListController(repository)
get_random_controller = GetRandomController(repository)

product_routes = Blueprint('product_routes', __name__)


@product_routes.route('/list/<string:survey_id>', methods=['GET'])
def get_all(survey_id: str):
    return list_controller.run(survey_id)


@product_routes.route('/<string:product_id>', methods=['GET'])
def get(product_id: str):
    return get_controller.run(product_id)


@product_routes.route('/random/<string:survey_id>', methods=['GET'])
def get_random(survey_id: str):
    return get_random_controller.run(survey_id)


@product_routes.route('/', methods=['POST'])
def create():
    return create_controller.run(request)
