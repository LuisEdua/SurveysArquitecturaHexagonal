from sqlalchemy import Column, String
from Database.MySQL import Base


class MySQLUserModel(Base):
    __tablename__ = 'Users'
    uuid = Column(String(36), primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    cellphone = Column(String(20), nullable=False)
