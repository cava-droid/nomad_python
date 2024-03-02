# 5.7 Code Challenge


class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def show_players(self):
        for player in self.players:
            player.introduce()


team_x = Team("Team X")
team_blue = Team("Team Blue")


# nico = Player(
#     name="nico",
#     team="Team X",
# )

# lynn = Player(
#     name="lynn",
#     team="Team Blue",
# )

team_x.add_player("nico")
# team_blue = team_blue.add_player("Lynn")  이렇게 쓰면 에러;;;
team_blue.add_player("Lynn")

team_x.show_players()
team_blue.show_players()
