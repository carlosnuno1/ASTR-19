class Animal:
    def __init__(self, lengthOfArms, lengthOfLegs, eyes, tail, furry):
        self.lengthOfArms = lengthOfArms
        self.lengthOfLegs = lengthOfLegs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry

    def describe(self):
        print(f"Arm length is: ", self.lengthOfArms)
        print(f"Leg Length is: ", self.lengthOfLegs)
        print(f"Number of eyes: ", self.eyes)
        print(f"Has tail: ", self.tail)
        print(f"Is furry: ", self.furry)

favoriteAnimal = Animal(1.3, 1.3, 2, True, True)

print(favoriteAnimal)
favoriteAnimal.describe()
