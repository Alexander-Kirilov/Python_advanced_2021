class PizzaDelivery:

    def __init__(self, name, price, ingredients={}):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if ingredient in self.ingredients:
            pass
