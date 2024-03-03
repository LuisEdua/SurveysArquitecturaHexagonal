from Database.MySQL import engine, Base, session_local
from AdminSurveys.Domain.Entity.Survey import Survey
from AdminSurveys.Domain.Port.SurveyPort import SurveyPort
from AdminSurveys.Infrestructure.Models.MySQLSurveyModel import MySQLSurveyModel as Model


class MySQLSurveyRepository(SurveyPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def list_surveys(self, user_id):
        surveys = self.db.query(Model).filter(Model.user_id == user_id).all()
        if len(surveys) == 0:
            return {"message": "No surveys", "status": False}
        else:
            return {"message": "Surveys found", "status": True, "surveys": [self.response(s) for s in surveys]}

    def get_survey(self, survey_id):
        survey = self.db.query(Model).filter(Model.uuid == survey_id).first()
        if survey is None:
            return {"message": "Survey not found", "status": False}
        else:
            return {"message": "Survey found", "status":True, "survey":self.response(survey)}

    def add_survey(self, survey: Survey):
        model = Model(uuid=survey.uuid, title=survey.title, description=survey.description, user_id=survey.user_id)
        self.db.add(model)
        self.db.commit()
        return {"message": "Survey added", "status": True, "survey": self.response(model)}

    def update_survey(self, survey_id, title, description):
        survey = self.db.query(Model).filter(Model.uuid == survey_id).first()
        survey.title = title if title is not None else survey.title
        survey.description = description if description is not None else survey.description
        self.db.commit()
        return {"message": "Survey updated", "status": True, "survey":self.response(survey)}

    def delete_survey(self, survey_id):
        survey = self.db.query(Model).filter(Model.uuid == survey_id).first()
        self.db.delete(survey)
        self.db.commit()
        return {"message": "Survey deleted", "status": True}

    @staticmethod
    def response(model: Model):
        return {"uuid": model.uuid, "title": model.title, "description": model.description, "user": model.user.user_name}
