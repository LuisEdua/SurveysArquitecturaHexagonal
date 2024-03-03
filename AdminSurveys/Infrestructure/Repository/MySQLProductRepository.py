import random
from Database.MySQL import engine, Base, session_local
from AdminSurveys.Domain.Entity.Product import Product
from AdminSurveys.Domain.Port.ProductPort import ProductPort
from AdminSurveys.Infrestructure.Models.MySQLProductModel import MySQLProductModel as Model


class MySQLProductRepository(ProductPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_random_product(self, survey_id):
        products = self.db.query(Model).filter(Model.survey_id == survey_id).all()
        if not products:
            return {"message": "Prodcts not found", "status": False}
        else:
            product = random.choice(products)
            return {"message": "Prodcts found", "status": True, "products": self.response(product)}

    def get_product(self, product_id):
        product = self.db.query(Model).filter(Model.product_id == product_id).first()
        if not product:
            return {"message": "Product not found", "status": False}
        else:
            return {"message": "Product found", "status": True, "product": self.response(product)}

    def list_products(self, survey_id):
        products = self.db.query(Model).filter(Model.survey_id == survey_id).all()
        if not products:
            return {"message": "Prodcts not found", "status": False}
        else:
            return {"message": "Prodcts found", "status": True, "products": [self.response(p) for p in products]}

    def create_product(self, product: Product):
        model = Model(uuid=product.uuid, survey_id=product.survey_id, name=product.name,
                      description=product.description)
        self.db.add(model)
        self.db.commit()
        return {"message": "Product created", "status": True, "product": self.response(model)}

    @staticmethod
    def response(model: Model):
        return {"uuid": model.uuid, "name": model.name, "description": model.description, "survey": model.surver.title}
