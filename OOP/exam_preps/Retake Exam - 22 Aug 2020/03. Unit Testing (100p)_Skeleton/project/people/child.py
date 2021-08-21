class Child:
    def __init__(self, food_cost, *toy_costs):
        self.cost = food_cost + sum(toy_costs)
