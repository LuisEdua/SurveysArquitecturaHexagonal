from Database.MySQL import Base, engine, session_local
from AdminSurveys.Domain.Entity.Answer import Answer
from AdminSurveys.Domain.Port.AnswerPort import AnswerPort
from AdminSurveys.Infrestructure.Models.MySQLAnswerModel import MySQLAnswerModel as Model
import random


class MySQLAnswerRepository(AnswerPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_answer(self, survey_id):
        answers = self.db.query(Model).filter(Model.survey_id == survey_id).all()
        if len(answers) < 1:
            return {"message": "answer not found", "status": False}
        else:
            return {"message": "answers found", "status": True, "answers": [self.response(a) for a in answers]}

    def add_answer(self, answer: Answer):
        model = Model(uuid=answer.uuid, survey_id=answer.survey_id, user_id=answer.user_id, answer=answer.answer)
        self.db.add(model)
        self.db.commit()
        receive_gift = True if random.random() < 0.10 else False
        return {"message": "Answer added", "status": True, "answer": self.response(model), "receive_gift": receive_gift}

    @staticmethod
    def response(model: Model):
        return {"uuid": model.uuid, "answer": model.answer, 'user': model.user.user_name,
                'question': model.survey.title}
