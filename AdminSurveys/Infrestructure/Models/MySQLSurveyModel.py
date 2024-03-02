from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from Database.MySQL import Base
from MySQLUserModel import MySQLUserModel as User


class MySQLSurveyModel(Base):
    __tablename__ = 'surveys'
    uuid = Column(String(36), primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'))
    user = relationship(User, backref=backref('surveys', uselist=True))
