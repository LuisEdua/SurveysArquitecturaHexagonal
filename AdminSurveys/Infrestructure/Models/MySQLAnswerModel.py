from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from Database.MySQL import Base
from AdminSurveys.Infrestructure.Models.MySQLSurveyModel import MySQLSurveyModel as Survey
from AdminSurveys.Infrestructure.Models.MySQLUserModel import MySQLUserModel as User


class MySQLAnswerModel(Base):
    __tablename__ = 'answers'
    uuid = Column(String(36), primary_key=True)
    answer = Column(String(255), nullable=False)
    user_id = Column(String(36), ForeignKey('users.uuid'))
    survey_id = Column(String(36), ForeignKey('surveys.uuid'))
    user = relationship(User, backref=backref('answers', uselist=True))
    survey = relationship(Survey, backref=backref('answers', uselist=True))
