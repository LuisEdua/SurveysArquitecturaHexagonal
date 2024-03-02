import uuid


class Product:
    def __init__(self, name, survey_id, description):
        self.uuid = uuid.uuid4()
        self.name = name
        self.survey_id = survey_id
        self.description = description
