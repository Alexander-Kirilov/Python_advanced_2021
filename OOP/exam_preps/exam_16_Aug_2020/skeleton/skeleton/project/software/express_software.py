from project.software.software import Software


class ExpressSoftware (Software):
    _TYPE = "Light"
    _MEMORY_CONSUMPTION_COEFFICIENT = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         ExpressSoftware ._TYPE, memory_consumption,
                         int(memory_consumption * ExpressSoftware ._MEMORY_CONSUMPTION_COEFFICIENT))
