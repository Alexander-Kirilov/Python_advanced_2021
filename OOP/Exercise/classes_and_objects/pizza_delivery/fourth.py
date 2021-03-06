class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * ingredient_price

    def make_order(self):
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([k+': '+str(v) for k, v in self.ingredients.items()])} and the price will be {self.price}lv."


