# Class Inheritance enables another class to grab all methods that are in another class

class Person: 
    def move(self):
        print("Moves 5 paces forward")
    def heal(self):
        print("Gain 3 HP more")

class Doctor(Person):
    def heal(self):
        print("Gain 10 HP more")

class Fighter(Person):
    def move(self):
        print("Move 15 paces forward")
    def fight(self):
        print("Deals 5 HP damage")

class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print("All enemies are asleep now. He he")

character1 = Person() 
character1.move()

character2 = Wizard()
character2.heal()

