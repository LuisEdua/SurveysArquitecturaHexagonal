from flask import Flask
from AdminSurveys.Infrestructure.Routes.UserRoute import user_routes
from AdminSurveys.Infrestructure.Routes.SurveyRoute import survey_routes
from AdminSurveys.Infrestructure.Routes.AnswerRoute import answer_routes
from AdminSurveys.Infrestructure.Routes.ProductRoute import product_routes

app = Flask(__name__)


app.register_blueprint(answer_routes, url_prefix="/answer")
app.register_blueprint(product_routes, url_prefix="/product")
app.register_blueprint(survey_routes, url_prefix="/survey")
app.register_blueprint(user_routes, url_prefix="/user")

if __name__ == '__main__':
    app.run()
