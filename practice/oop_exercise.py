# Create a class person w 2 attributes & 2 methods
class Person:
    def __init__(self, name: str, age=0):
        assert age > 10 
        #This is my constructor, assign self to object
        self.name = name
        self.age = age
    
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"name:{self.name}, age:{self.age}"

# Create happy_birthday method that adds 1 year to age
    def happy_birthday(self): 
        self.age += 1 

# Create change_name method that changes name of person
    def change_name(self, new_name):
        self.name = new_name

p1 = Person("John", 35)
p2 = Person("Alexa", 33)

# Create a class office w 2 attributes, a constructor, and 2 methods
class Office:

# Constructor that initialise people_working as an empty list
    def __init__(self, name: str):
        self.name = name
        self.people_working = []

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"office:{self.name}, people workig are:{self.people_working}"

# Create start_working_for method that takes an object of Person and adds it to people_working
    def start_working_for(self, person ):
        self.people_working.append(person)

#Create finished_working_for method that removes it from the people_working
    def finished_working_for(self, person ):
        self.people_working.remove(person)


office = Office("default")

# Create an object of the class names Ecorus
office_ecorus = Office("Ecorus")
office.people_working = [Person("Kleo", 28)]
office.start_working_for(p1)
office.start_working_for(p2)

# Create 2 objects of that class
eduardo = Person("Eduardo", 35)
dev_eli = Person("dev_Eli", 27)

# Make Eduardo and dev_name start working for Ecorus
office_ecorus.start_working_for(eduardo)
office_ecorus.start_working_for(dev_eli)

# Make Eduardo finish working for Ecorus
office_ecorus.finished_working_for(eduardo)

print(office, office_ecorus)

