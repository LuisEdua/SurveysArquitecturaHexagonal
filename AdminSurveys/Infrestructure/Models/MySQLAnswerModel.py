from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from Database.MySQL import Base
from MySQLSurveyModel import MySQLSurveyModel as Survey
from MySQLUserModel import MySQLUserModel as User


class MySQLAnswerModel(Base):
    __tablename__ = 'answers'
    uuid = Column(String(36), primary_key=True)
    answer = Column(String(255), nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'))
    survey_id = Column(String(36), ForeignKey('survey.id'))
    user = relationship(User, backref=backref('answers', uselist=True))
    survey = relationship(Survey, backref=backref('answers', uselist=True))
