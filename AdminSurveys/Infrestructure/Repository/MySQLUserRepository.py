from sqlalchemy.sql.functions import user

from Database.MySQL import session_local, Base, engine
from AdminSurveys.Domain.Entity.User import User
from AdminSurveys.Domain.Port.UserPort import UserPort
from AdminSurveys.Infrestructure.Models.MySQLUserModel import MySQLUserModel as Model
import bcrypt


class MySQLUserRepository(UserPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def login(self, email, password):
        model = self.db.query(Model).filter_by(email=email).first()
        if not model:
            return {"message": "Email not found", "status": False}
        elif bcrypt.checkpw(password.encode('utf-8'), model.password.encode('utf-8')):
            return {"message": "Login successful", "status": True, "user": self.response(model)}
        else:
            return {"message": "Password incorrect", "status": False}

    def register(self, user: User):
        model = Model(uuid=user.uuid, email=user.email, password=user.password,
                      user_name=user.user_name, cellphone=user.phone_number)
        self.db.add(model)
        self.db.commit()
        return {"message": "User created successfully", "status": True, "user": self.response(model)}

    @staticmethod
    def response(model: Model):
        return {"uuid": model.uuid, "name": model.user_name, "email": model.email, "cellphone": model.cellphone}
