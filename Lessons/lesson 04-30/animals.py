class Animal:

    def eat(self, food):
        print(f"eating {food}")

class Carnivore(Animal):

    def eat(self, food):
        if food == "meat":
            Animal.eat(self, food)
        else: 
            print("I will not eat this")

class Herbivore(Animal):

    def eat(self, food):
        if food == "grass":
            Animal.eat(self, food)
        else: 
            print("I will not eat this")

class Omnivore(Carnivore, Herbivore):

    def eat(self, food):
        if food == "meat":
            Carnivore.eat(self, food)
        elif food == "grass":
            Herbivore.eat(self, food)
        else:
            print("I will not eat this")

meat = "meat"
grass = "grass"
leo = Carnivore()
elephant = Herbivore()
human = Omnivore()

animals = [leo, elephant, human]
for animal in animals:
    print(animal)
    animal.eat(meat)
    animal.eat(grass)