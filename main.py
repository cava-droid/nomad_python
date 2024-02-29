# 5.1 Why We Need OOP

# nico = {
#     "name": "Nico",
#     "XP": 1000,
#     "team": "Team X",
# }

def create_player_team(name, xp, team):
    pass

def create_player(name, xp, team):
    return {
        "name": "Nico",
        "XP": 1000,
        "team": "Team X",
    }

def introduce_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")

nico = create_player("Nico", 1500, "Team X")    
introduce_player(nico)
