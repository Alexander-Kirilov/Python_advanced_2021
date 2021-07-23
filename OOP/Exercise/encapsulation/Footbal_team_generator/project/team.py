class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__player = []

    def add_player(self, player):
        if player in self.__player:
            return f"Player {player.name} has already joined"
        self.__player.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for player in self.__player:
            if player.name == player_name:
                self.__player.remove(player)
                return player
        return f"Player {player_name} not found"
