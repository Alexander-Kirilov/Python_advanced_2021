from Wild_cat_zoo.project import Product


class Drink(Product):

    def __init__(self, name):
        super().__init__(name, 10)
