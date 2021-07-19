class Dog:
    kind = 'canine'  # class variable shared by all instances           class attribute

    def __init__(self, name):                                           # init method
        self.name = name
        self.tricks = []  # creates empty list for each dog             instance attribute

    def add_trick(self, trick):                                         # instance method
        self.tricks.append(trick)


poodle = Dog("Bella")  # instance
beagle = Dog("Max")
print(poodle.name, poodle.kind)  # Bella canine
print(beagle.name, beagle.kind)  # Max canine
poodle.tricks.append('roll over')
beagle.tricks.append('play dead')
print(poodle.tricks)  # ['roll over']
print(beagle.tricks)  # ['play dead']
