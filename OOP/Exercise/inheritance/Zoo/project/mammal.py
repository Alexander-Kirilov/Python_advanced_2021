from project.animal import Animal


class Mammal(Animal):
    pass

    @property
    def name(self):
        return self.__name