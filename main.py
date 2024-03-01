# 5.4 Inheritance


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


class GuardDog(Dog):
    def rrrr(self):
        print("stay away!")


class Puppy(Dog):
    def woof_woof(self):
        print("Woof Woof!")


ruffus = Puppy(
    name="Ruffus",
    breed="Beagle",
    age=0.1,
)

bibi = Puppy(
    name="Bibi",
    breed="Dalmatian",
    age=0.1,
)
