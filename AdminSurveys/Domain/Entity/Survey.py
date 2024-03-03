import uuid


class Survey:
    def __init__(self, title, description, user_id):
        self.uuid = uuid.uuid4()
        self.title = title
        self.description = description
        self.user_id = user_id
