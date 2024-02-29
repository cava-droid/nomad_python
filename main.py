# 5.3 Methods


class Puppy:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed

    def __str__(self):
        return f"{self.breed} puppy named {self.name}"


ruffus = Puppy(
    name="Ruffus",
    breed="Beagle",
)
bibi = Puppy(
    name="Bibi",
    breed="Dalmatian",
)

print(
    bibi,
    ruffus,
)

# print(ruffus.name)
# print(ruffus.age)
# print(ruffus.breed)
# print()
# print(bibi.name)
# print(bibi.age)
# print(bibi.breed)
