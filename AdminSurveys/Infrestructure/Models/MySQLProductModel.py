from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from Database.MySQL import Base
from AdminSurveys.Infrestructure.Models.MySQLSurveyModel import MySQLSurveyModel as Survey


class MySQLProductModel(Base):
    __tablename__ = 'products'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    survey_id = Column(String(36), ForeignKey('surveys.uuid'))
    survey = relationship(Survey, backref=backref('products', uselist=True))
