from project.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, calories, grams):
        self.__calories = calories
        super().__init__(name, price, grams)

    @property
    def calories(self):
        return self.__calories
