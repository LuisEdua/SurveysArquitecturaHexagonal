import uuid
import bcrypt


class User:
    def __init__(self, email, password, user_name, phone_number):
        self.uuid = uuid.uuid4()
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')
        self.user_name = user_name
        self.phone_number = phone_number
