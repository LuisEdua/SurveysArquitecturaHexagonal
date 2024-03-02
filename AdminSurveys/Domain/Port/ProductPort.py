from abc import ABC, abstractmethod
from AdminSurveys.Domain.Entity.Product import Product


class ProductPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_product(self, product_id):
        pass

    @abstractmethod
    def list_products(self, survey_id):
        pass

    @abstractmethod
    def create_product(self, product:Product):
        pass
